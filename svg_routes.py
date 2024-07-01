def generate_svg(username, position, crVulnerability, crBusinessRisk):
    svg_template = f'''
   <svg xmlns="http://www.w3.org/2000/svg" width="470" height="180">
  <rect x="0" y="0" width="470" height="165" rx="20" ry="20" fill="url(#MyGradient)" />

    <text x="30" y="40" fill="white" font-size="25" font-weight="bold" font-family="Arial">
    STANDOFF365 metrics
  </text>
    
  <text x="30" y="80" fill="white" font-size="13" font-weight="bold" font-family="Arial">
    Username: </text>
   <text x="110" y="80" fill="#00ff33" font-size="13" font-weight="bold" font-family="Arial">
    {username}</text>
  <text x="75%" y="80" dominant-baseline="middle" text-anchor="middle" fill="white" font-size="17" font-weight="bold" font-family="Arial">
    CYBERRANGE RATING </text>
   <text x="75%" y="67%" dominant-baseline="middle" text-anchor="middle" fill="#ff0000" font-size="70" font-weight="bold" font-family="Arial">
    {position}</text>
  <text x="30" y="102" fill="white" font-size="13" font-weight="bold" font-family="Arial">
    Vuln score: </text>
   <text x="110" y="102" fill="#00ff33" font-size="13" font-weight="bold" font-family="Arial">
    {crVulnerability}</text>
   <text x="30" y="125" fill="white" font-size="13" font-weight="bold" font-family="Arial">
    Buisness Risc score: </text>
   <text x="170" y="125" fill="#00ff33" font-size="13" font-weight="bold" font-family="Arial">
    {crBusinessRisk}</text>
<defs>
        <linearGradient id="MyGradient">
          <stop offset="5%" stop-color="#660033" />
          <stop offset="95%" stop-color="#0e1231" />
        </linearGradient>
      </defs>
</svg>
    '''
    return svg_template


def generatebb_svg(username, bbPosition, bbReportsCount):
    bbsvg_template = f'''
   <svg xmlns="http://www.w3.org/2000/svg" width="300" height="70" fill="none">
    <rect width="220" height="20" y="48" x="10" rx="10" fill="url(#grad)" stroke="#FFFFFF" stroke-width="2"  />
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color: #4f0014; stop-opacity: 1" />
      <stop offset="100%" style="stop-color: #252850; stop-opacity: 1" />
    </linearGradient>
  </defs>
  <polygon points="10,0 120,0 190,50 10,50" fill="#470736" rx="10" />
  <rect width="300" height="35" y="15" rx="10" fill="url(#grad)" stroke="#FFFFFF" stroke-width="2"  />
  <text x="10" y="38" fill="#f5f5f5" font-size="20" font-weight="bold" font-family="Arial">
    BugBounty Rating:</text>
   <text x="215" y="41" fill="#88f000" font-size="28" font-weight="bold" font-family="Arial">
    {bbPosition}</text>
    <text x="25" y="10" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    STANDOFF365</text>
   <text x="25" y="63" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    BugBounty report count:  </text>
 <text x="220" y="63" text-anchor="end" fill="#00ffa6" font-size="13" font-weight="bold" font-family="Arial">
  {bbReportsCount}
</text>
</svg>

    '''
    return bbsvg_template