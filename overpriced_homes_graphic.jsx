export default function OverpricedHomesGraphic() {
  // DATA — Las Vegas MLS Jan–Mar 2026
  const data = {
    pricedRight: {
      listPrice: 547000,
      soldPrice: 542000,
      soldRatio: 8,
      dom: 13,
      saleToList: 99,
    },
    overpriced: {
      listPrice: 611000,
      soldPrice: 597000,
      soldRatio: 5,
      dom: 119,
      saleToList: 98,
    },
    gap: 14290,
    handle: "@rosehomeslv",
  };

  // BRANDING — Rose Homes LV
  const colors = {
    primary: "#1a2e4a",
    accent: "#c9973a",
    background: "#f5f4f1",
    text: "#0f0f0f",
    secondaryText: "#666666",
    rule: "#d6d2cc",
    ghostStrokePrimary: "#8fa3bb",
    ghostStrokeAccent: "#e0b87a",
    font: "Georgia, serif",
  };

  const fmt = (n) =>
    "$" + n.toLocaleString("en-US", { maximumFractionDigits: 0 });

  // House pictogram component
  const Houses = ({ filled, filledColor, ghostStroke, y }) => {
    const houses = [];
    for (let i = 0; i < 10; i++) {
      const x = 160 + i * 58;
      const isFilled = i < filled;
      houses.push(
        <g key={i} transform={`translate(${x}, ${y})`}>
          {/* Roof */}
          <polygon
            points="23,0 46,22 0,22"
            fill={isFilled ? filledColor : "none"}
            stroke={isFilled ? filledColor : ghostStroke}
            strokeWidth={isFilled ? 0 : 1.6}
          />
          {/* Body */}
          <rect
            x={3.7}
            y={22}
            width={38.6}
            height={24}
            rx={1.5}
            fill={isFilled ? filledColor : "none"}
            stroke={isFilled ? filledColor : ghostStroke}
            strokeWidth={isFilled ? 0 : 1.6}
          />
          {/* Door */}
          <rect
            x={16.6}
            y={30}
            width={12.8}
            height={16}
            rx={1}
            fill={isFilled ? colors.background : "none"}
            stroke={isFilled ? "none" : ghostStroke}
            strokeWidth={isFilled ? 0 : 1.2}
          />
        </g>
      );
    }
    return <>{houses}</>;
  };

  return (
    <div style={{ maxWidth: 540, margin: "0 auto", fontFamily: colors.font }}>
      <svg
        viewBox="0 0 1080 1080"
        width="100%"
        xmlns="http://www.w3.org/2000/svg"
        style={{ display: "block", background: colors.background }}
      >
        {/* Background */}
        <rect width={1080} height={1080} fill={colors.background} />

        {/* Top label */}
        <text
          x={540}
          y={110}
          textAnchor="middle"
          fontSize={12}
          letterSpacing={5}
          fill={colors.secondaryText}
          fontFamily={colors.font}
        >
          THE TRUTH ABOUT PRICING
        </text>

        {/* Headline */}
        <text
          x={540}
          y={210}
          textAnchor="middle"
          fontSize={48}
          fontWeight={600}
          fill={colors.primary}
          fontFamily={colors.font}
        >
          Overpriced homes
        </text>
        <text
          x={540}
          y={270}
          textAnchor="middle"
          fontSize={48}
          fontWeight={600}
          fill={colors.primary}
          fontFamily={colors.font}
        >
          don't just sell slower.
        </text>

        {/* Accent headline */}
        <text
          x={540}
          y={370}
          textAnchor="middle"
          fontSize={52}
          fontWeight={600}
          fontStyle="italic"
          fill={colors.accent}
          fontFamily={colors.font}
        >
          They sell for less.
        </text>

        {/* Rule 1 */}
        <line
          x1={160}
          y1={435}
          x2={920}
          y2={435}
          stroke={colors.rule}
          strokeWidth={1}
        />

        {/* Priced Right label row */}
        <text
          x={160}
          y={475}
          fontSize={12}
          letterSpacing={3.5}
          fill={colors.text}
          fontFamily={colors.font}
          fontWeight={600}
        >
          PRICED RIGHT
        </text>
        <text
          x={920}
          y={475}
          textAnchor="end"
          fontSize={19}
          fill={colors.secondaryText}
          fontFamily={colors.font}
        >
          Listed at {fmt(data.pricedRight.listPrice)}
        </text>

        {/* Priced Right houses */}
        <Houses
          filled={data.pricedRight.soldRatio}
          filledColor={colors.primary}
          ghostStroke={colors.ghostStrokePrimary}
          y={500}
        />

        {/* Priced Right results */}
        <text
          x={160}
          y={582}
          fontSize={16}
          fill={colors.secondaryText}
          fontFamily={colors.font}
        >
          {data.pricedRight.soldRatio} of 10 sold within {data.pricedRight.dom}{" "}
          days
        </text>
        <text
          x={160}
          y={614}
          fontSize={26}
          fontWeight={600}
          fill={colors.text}
          fontFamily={colors.font}
        >
          Sold for {fmt(data.pricedRight.soldPrice)}
        </text>
        <text
          x={160 + 310}
          y={614}
          fontSize={17}
          fontStyle="italic"
          fill={colors.secondaryText}
          fontFamily={colors.font}
        >
          — {data.pricedRight.saleToList}% of ask
        </text>

        {/* Rule 2 */}
        <line
          x1={160}
          y1={665}
          x2={920}
          y2={665}
          stroke={colors.rule}
          strokeWidth={1}
        />

        {/* Overpriced label row */}
        <text
          x={160}
          y={705}
          fontSize={12}
          letterSpacing={3.5}
          fill={colors.accent}
          fontFamily={colors.font}
          fontWeight={600}
        >
          OVERPRICED
        </text>
        <text
          x={920}
          y={705}
          textAnchor="end"
          fontSize={19}
          fill={colors.secondaryText}
          fontFamily={colors.font}
        >
          Listed at {fmt(data.overpriced.listPrice)}
        </text>

        {/* Overpriced houses */}
        <Houses
          filled={data.overpriced.soldRatio}
          filledColor={colors.accent}
          ghostStroke={colors.ghostStrokeAccent}
          y={730}
        />

        {/* Overpriced results */}
        <text
          x={160}
          y={812}
          fontSize={16}
          fill={colors.secondaryText}
          fontFamily={colors.font}
        >
          {data.overpriced.soldRatio} of 10 sold — after {data.overpriced.dom}+
          days and price cuts
        </text>
        <text
          x={160}
          y={844}
          fontSize={26}
          fontWeight={600}
          fill={colors.accent}
          fontFamily={colors.font}
        >
          Sold for {fmt(data.overpriced.soldPrice)}
        </text>
        <text
          x={160 + 310}
          y={844}
          fontSize={17}
          fontStyle="italic"
          fill={colors.secondaryText}
          fontFamily={colors.font}
        >
          — {data.overpriced.saleToList}% of ask
        </text>

        {/* Rule 3 */}
        <line
          x1={160}
          y1={895}
          x2={920}
          y2={895}
          stroke={colors.rule}
          strokeWidth={1}
        />

        {/* Kicker */}
        <text
          x={540}
          y={945}
          textAnchor="middle"
          fontSize={21}
          fontStyle="italic"
          fontWeight={600}
          fill={colors.accent}
          fontFamily={colors.font}
        >
          ${data.gap.toLocaleString()} less than what they originally asked for.
        </text>

        {/* Handle */}
        <text
          x={540}
          y={1010}
          textAnchor="middle"
          fontSize={14}
          letterSpacing={1.5}
          fill={colors.secondaryText}
          fontFamily={colors.font}
        >
          {data.handle}
        </text>
      </svg>
    </div>
  );
}
