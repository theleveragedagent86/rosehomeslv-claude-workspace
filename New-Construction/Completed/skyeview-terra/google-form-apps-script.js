/**
 * SkyeView Terra Google Form -> Lofty CRM Integration
 * ====================================================
 *
 * Copy and paste this entire file into the Google Apps Script editor for your
 * SkyeView Terra form. See google-form-setup.md for the full setup guide.
 *
 * What this does:
 *   1. Fires when a lead submits the Google Form
 *   2. Reads the form responses
 *   3. Calculates the smart plan track (Hot, Warm, or Nurture) from answers
 *   4. POSTs the lead data to Lofty's inbound webhook
 *   5. Logs the result so you can debug if something fails
 *
 * Setup time: 5 minutes
 * See: google-form-setup.md (Part 3, Option A)
 */


/* ============================================================
   CONFIGURATION - EDIT THESE TWO VALUES
   ============================================================ */

// 1. Paste your Lofty inbound webhook URL here.
//    Get this from: Lofty Settings > Integrations > Webhook URL
const LOFTY_WEBHOOK_URL = 'YOUR_LOFTY_WEBHOOK_URL_HERE';

// 2. Optional: Email address to BCC on every lead (useful for backup)
//    Leave as empty string '' if you do not want a backup email.
const BACKUP_EMAIL = 'ryan@rosehomeslv.com';


/* ============================================================
   COMMUNITY CONFIGURATION (already set for SkyeView Terra)
   ============================================================ */

const COMMUNITY = {
    name: 'SkyeView Terra',
    slug: 'skyeview-terra',
    builder: 'Century Communities',
    source: 'SkyeView Terra Landing Page'
};


/* ============================================================
   MAIN HANDLER - Fires on every form submit
   ============================================================ */

function onFormSubmit(e) {
    try {
        // Pull responses from the form submission event
        const responses = e.namedValues;

        // Field names must match your Google Form questions exactly.
        // If you renamed any questions, update the keys below.
        const fullName = (responses['Full Name'] || [''])[0].trim();
        const email = (responses['Email'] || [''])[0].trim().toLowerCase();
        const phone = cleanPhone((responses['Phone'] || [''])[0]);
        const timeline = (responses['When are you looking to buy?'] || [''])[0];
        const preApproved = (responses['Are you pre-approved for a mortgage?'] || [''])[0];

        // Split the full name into first and last
        const nameParts = fullName.split(/\s+/);
        const firstName = nameParts[0] || '';
        const lastName = nameParts.slice(1).join(' ') || '';

        // Calculate the smart plan track from the qualifying answers
        const track = calculateTrack(timeline, preApproved);

        // Build the payload Lofty will receive
        const payload = {
            // Standard contact fields
            firstName: firstName,
            lastName: lastName,
            email: email,
            phone: phone,

            // Lead routing
            source: COMMUNITY.source,
            tags: [COMMUNITY.slug],

            // Custom fields used by Lofty smart plan rules
            customField: {
                community: COMMUNITY.name,
                builder: COMMUNITY.builder,
                track: track,
                timeline: timeline,
                preApproved: preApproved
            },

            // Notes that will appear on the contact in Lofty
            notes:
                'Lead from ' + COMMUNITY.source + '\n' +
                'Community: ' + COMMUNITY.name + '\n' +
                'Builder: ' + COMMUNITY.builder + '\n' +
                'Timeline: ' + timeline + '\n' +
                'Pre-approved: ' + preApproved + '\n' +
                'Suggested track: ' + track.toUpperCase()
        };

        // Send to Lofty
        const result = postToLofty(payload);

        // Log success to Apps Script execution log
        Logger.log('SUCCESS: Lead pushed to Lofty');
        Logger.log('Name: ' + firstName + ' ' + lastName);
        Logger.log('Email: ' + email);
        Logger.log('Track: ' + track);
        Logger.log('Lofty response: ' + result);

        // Send backup email so you have a record even if Lofty fails silently
        if (BACKUP_EMAIL) {
            sendBackupEmail(payload);
        }

    } catch (err) {
        // If anything fails, log it and email yourself so the lead is not lost
        Logger.log('ERROR in onFormSubmit: ' + err.toString());
        Logger.log('Stack: ' + err.stack);

        if (BACKUP_EMAIL) {
            try {
                MailApp.sendEmail({
                    to: BACKUP_EMAIL,
                    subject: 'URGENT: SkyeView Terra lead failed to reach Lofty',
                    body:
                        'A lead submitted the SkyeView Terra Google Form, but the ' +
                        'Lofty integration failed. Please add this lead to Lofty ' +
                        'manually so the smart plan can start.\n\n' +
                        'Error: ' + err.toString() + '\n\n' +
                        'Form responses:\n' +
                        JSON.stringify(e.namedValues, null, 2)
                });
            } catch (emailErr) {
                Logger.log('Backup email also failed: ' + emailErr.toString());
            }
        }
    }
}


/* ============================================================
   POST TO LOFTY WEBHOOK
   ============================================================ */

function postToLofty(payload) {
    if (!LOFTY_WEBHOOK_URL || LOFTY_WEBHOOK_URL === 'YOUR_LOFTY_WEBHOOK_URL_HERE') {
        throw new Error('Lofty webhook URL is not configured. Edit LOFTY_WEBHOOK_URL at the top of the script.');
    }

    const options = {
        method: 'post',
        contentType: 'application/json',
        payload: JSON.stringify(payload),
        muteHttpExceptions: true,
        headers: {
            'Accept': 'application/json'
        }
    };

    const response = UrlFetchApp.fetch(LOFTY_WEBHOOK_URL, options);
    const responseCode = response.getResponseCode();
    const responseText = response.getContentText();

    if (responseCode < 200 || responseCode >= 300) {
        throw new Error(
            'Lofty webhook returned ' + responseCode + ': ' + responseText
        );
    }

    return responseText;
}


/* ============================================================
   SMART PLAN TRACK LOGIC
   ============================================================
   Matches the rules in smart-plan.md:
     Hot     = ASAP or 1 to 3 months AND pre-approved
     Warm    = 1 to 3 or 3 to 6 months AND any pre-approval status
     Nurture = Just browsing
*/

function calculateTrack(timeline, preApproved) {
    const t = (timeline || '').toLowerCase();
    const p = (preApproved || '').toLowerCase();

    const isShortTimeline = t.indexOf('asap') !== -1 || t.indexOf('1 to 3') !== -1;
    const isMidTimeline = t.indexOf('1 to 3') !== -1 || t.indexOf('3 to 6') !== -1;
    const isJustBrowsing = t.indexOf('browsing') !== -1;
    const isPreApproved = p.indexOf('yes') !== -1;

    if (isJustBrowsing) {
        return 'nurture';
    }
    if (isShortTimeline && isPreApproved) {
        return 'hot';
    }
    return 'warm';
}


/* ============================================================
   PHONE NUMBER CLEANUP
   ============================================================ */

function cleanPhone(rawPhone) {
    if (!rawPhone) return '';
    // Strip everything that is not a digit
    const digits = rawPhone.replace(/[^0-9]/g, '');
    // If it starts with 1 and has 11 digits, drop the leading 1
    if (digits.length === 11 && digits.charAt(0) === '1') {
        return digits.substring(1);
    }
    return digits;
}


/* ============================================================
   BACKUP EMAIL (optional)
   ============================================================ */

function sendBackupEmail(payload) {
    const subject = 'New SkyeView Terra Lead: ' + payload.firstName + ' ' + payload.lastName;
    const body =
        'A new lead just came in through the SkyeView Terra landing page.\n\n' +
        'Name: ' + payload.firstName + ' ' + payload.lastName + '\n' +
        'Email: ' + payload.email + '\n' +
        'Phone: ' + payload.phone + '\n\n' +
        'Timeline: ' + payload.customField.timeline + '\n' +
        'Pre-approved: ' + payload.customField.preApproved + '\n' +
        'Smart plan track: ' + payload.customField.track.toUpperCase() + '\n\n' +
        'This lead has been pushed to Lofty CRM. The smart plan should be ' +
        'starting now. Check Lofty to confirm.\n\n' +
        '---\n' +
        'Source: ' + payload.source + '\n' +
        'Tag applied: ' + payload.tags[0];

    MailApp.sendEmail({
        to: BACKUP_EMAIL,
        subject: subject,
        body: body
    });
}


/* ============================================================
   MANUAL TEST FUNCTION
   ============================================================
   Use this to verify the integration works before going live.

   1. In the Apps Script editor, select 'testIntegration' from the function
      dropdown next to the Run button
   2. Click Run
   3. Approve permissions
   4. Check Lofty for a contact named 'Test Lead'
   5. Delete the test contact in Lofty when done
*/

function testIntegration() {
    const fakeEvent = {
        namedValues: {
            'Full Name': ['Test Lead'],
            'Email': ['test+skyeviewterra@rosehomeslv.com'],
            'Phone': ['7025551234'],
            'When are you looking to buy?': ['1 to 3 months'],
            'Are you pre-approved for a mortgage?': ['Yes']
        }
    };

    onFormSubmit(fakeEvent);
    Logger.log('Test complete. Check Lofty CRM and your Apps Script execution log.');
}
