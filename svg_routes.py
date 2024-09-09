def generate_svg(position, crPosition, bbPosition, username, total,bbTotal ,crTotal ,bbReportsCount ,crReportsCount ,crVulnerability ,crBusinessRisk):
    svg_template = f'''
      <svg xmlns="http://www.w3.org/2000/svg" width="300" height="280" fill="none">
    <rect width="220" height="20" y="48" x="10" rx="10" fill="url(#grad)" stroke="#FFFFFF" stroke-width="2"  />
         <rect width="220" height="20" y="68" x="10" rx="10" fill="url(#grad)" stroke="#FFFFFF" stroke-width="2"  />
         <rect width="220" height="20" y="88" x="10" rx="10" fill="url(#grad)" stroke="#FFFFFF" stroke-width="2"  />
         <rect width="220" height="20" y="108" x="10" rx="10" fill="url(#grad)" stroke="#FFFFFF" stroke-width="2"  />
         <rect width="220" height="20" y="128" x="10" rx="10" fill="url(#grad)" stroke="#FFFFFF" stroke-width="2"  />
         <rect width="220" height="20" y="148" x="10" rx="10" fill="url(#grad)" stroke="#FFFFFF" stroke-width="2"  />
         <rect width="220" height="20" y="168" x="10" rx="10" fill="url(#grad)" stroke="#FFFFFF" stroke-width="2"  />
           <rect width="220" height="20" y="188" x="10" rx="10" fill="url(#grad)" stroke="#FFFFFF" stroke-width="2"  />
           <rect width="220" height="20" y="208" x="10" rx="10" fill="url(#grad)" stroke="#FFFFFF" stroke-width="2"  />
           <rect width="220" height="20" y="228" x="10" rx="10" fill="url(#grad)" stroke="#FFFFFF" stroke-width="2"  />
           <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color: #4f0014; stop-opacity: 1" />
      <stop offset="100%" style="stop-color: #252850; stop-opacity: 1" />
    </linearGradient>
  </defs>
  <polygon points="10,0 120,0 190,50 10,50" fill="#470736" rx="10" />
  <rect width="300" height="35" y="15" rx="10" fill="url(#grad)" stroke="#FFFFFF" stroke-width="2"  />
  <text x="10" y="38" fill="#f5f5f5" font-size="20" font-weight="bold" font-family="Arial">
    Cyberrange Rating:</text>
   <text x="292" y="41" fill="#88f000" text-anchor="end" font-size="28" font-weight="bold" font-family="Arial">
    {crPosition}</text>
    <text x="25" y="10" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    STANDOFF365</text>
   <text x="25" y="63" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    Username:  </text>
   <text x="25" y="83" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    Total rating:  </text>
   <text x="25" y="103" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    BugBounty rating:  </text>
   <text x="25" y="123" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    Tolal score:  </text>
   <text x="25" y="143" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    BugBounty score:  </text>
   <text x="25" y="163" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    Cyberrange score:  </text>
   <text x="25" y="183" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    BugBounty report count:  </text>
   <text x="25" y="203" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    Cyberrange report count:  </text>
   <text x="25" y="223" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    Vulnerability score:  </text>
   <text x="25" y="243" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    Business Risk score:  </text>

 <text x="220" y="63" text-anchor="end" fill="#00ffa6" font-size="13" font-weight="bold" font-family="Arial">
  {username}
</text>
 <text x="220" y="83" text-anchor="end" fill="#00ffa6" font-size="13" font-weight="bold" font-family="Arial">
  {position}
</text>
     
 <text x="220" y="103" text-anchor="end" fill="#00ffa6" font-size="13" font-weight="bold" font-family="Arial">
  {bbPosition}
</text>
 <text x="220" y="123" text-anchor="end" fill="#00ffa6" font-size="13" font-weight="bold" font-family="Arial">
  {total}
</text>
 <text x="220" y="143" text-anchor="end" fill="#00ffa6" font-size="13" font-weight="bold" font-family="Arial">
  {bbTotal}
</text>
 <text x="220" y="163" text-anchor="end" fill="#00ffa6" font-size="13" font-weight="bold" font-family="Arial">
  {crTotal}
</text>
 <text x="220" y="183" text-anchor="end" fill="#00ffa6" font-size="13" font-weight="bold" font-family="Arial">
  {bbReportsCount}
</text>
  <text x="220" y="203" text-anchor="end" fill="#00ffa6" font-size="13" font-weight="bold" font-family="Arial">
  {crReportsCount}
</text>
  <text x="220" y="223" text-anchor="end" fill="#00ffa6" font-size="13" font-weight="bold" font-family="Arial">
  {crVulnerability}
</text>
  <text x="220" y="243" text-anchor="end" fill="#00ffa6" font-size="13" font-weight="bold" font-family="Arial">
  {crBusinessRisk}
</text>

</svg> 

    '''
    return svg_template


def generatebb_svg(username, bbPosition,signal,impact,reportsTotal,reportsFinished,reportsInProgress,reportsAccepted,reportsInformational,reportsDuplicate,reportsOutOfScope,reportsRejected,reportsAbuse):
    bbsvg_template = f'''

<svg width="557" height="175" viewBox="0 0 557 175" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M78.3416 15.2544L81.4882 8.60006L84.6349 15.2544H78.3416ZM75.2134 1.4729L64.2725 26.8876H73.6139L75.4507 22.6196H87.5227L89.3595 26.8876H98.7533L87.8124 1.4729H75.2134Z" fill="white"/>
<path d="M151.371 19.9694H144.489V8.45212H151.371C155.717 8.45212 157.245 11.0315 157.245 14.2124C157.245 17.3932 155.313 19.9694 151.371 19.9694ZM151.84 1.4729H135.142V5.34524V6.81827V23.0699V23.9543V26.8843H151.92C158.213 26.8843 165.715 23.9962 165.715 14.177C165.715 3.3158 158.928 1.4729 151.84 1.4729Z" fill="white"/>
<path d="M184.537 20.3167C179.337 20.3167 176.943 17.6826 176.943 13.9968C176.943 10.028 179.343 7.67689 184.435 7.67689C189.021 7.67689 192.269 9.76423 192.269 13.9968C192.266 18.3709 189.273 20.3167 184.537 20.3167ZM184.234 1C173.284 1 168.023 5.00421 168.023 13.524C168.023 22.642 172.825 27 184.456 27C195.789 27 201.185 23.9124 201.185 14C201.185 3.86888 194.821 1 184.234 1Z" fill="white"/>
<path d="M230.695 9.14057V1.36694H254.882V5.5191V7.6804V26.8877H246.083H245.224H244.712V19.0852H230.695V11.6203H244.712V9.14057H230.695Z" fill="white"/>
<path d="M68.5786 9.91221V1.38599H36.3291V9.91221H47.7785V26.8875H48.0159H48.4103H56.5005H56.895H57.1292V9.91221H68.5786Z" fill="white"/>
<path d="M122.407 14.8781L111.904 1.38599H100.627V9.16283V9.7514V26.8875H108.717H109.506H109.978V13.1413L120.687 26.8875H131.755V19.1106V18.5221V1.38599H122.407V14.8781Z" fill="white"/>
<path d="M213.754 9.14057H227.771V1.36694H203.584V5.5191V7.6804V26.8877H212.383H213.243H213.754V19.0852H227.771V11.6203H213.754V9.14057Z" fill="white"/>
<path d="M19.1311 26.833C25.1841 26.833 29.1906 26.6143 31.7548 25.4854C34.3837 24.3307 35.5055 22.2209 35.5055 18.429C35.5055 16.8562 35.185 15.5987 34.5255 14.5856C34.3036 14.2446 33.8906 13.833 33.7981 13.7558C33.0893 13.1704 32.1308 12.733 30.7809 12.3824C30.7532 12.376 28.0534 11.6138 23.4705 11.2214C23.2301 11.1989 22.962 11.1764 22.6538 11.1474C21.8124 11.0702 20.6628 10.9609 19.0972 10.8515C18.0709 10.7808 17.1772 10.7422 16.3882 10.71C15.6516 10.6778 15.0136 10.6521 14.5051 10.6071C14.3818 10.5974 14.2401 10.5846 14.0798 10.5717C12.4371 10.4431 10.8314 10.2662 10.7944 9.65509C10.7667 9.16622 11.2259 8.69987 12.3909 8.5487C13.5774 8.39432 14.1291 8.33965 15.667 8.33965C17.3898 8.33965 21.7384 8.54549 22.7339 8.73203C23.2301 8.82208 23.5907 8.94752 23.939 9.14692C24.2595 9.33025 24.503 9.58111 24.6262 9.85449H34.5809L34.5686 9.49749C34.2912 2.71446 30.5929 1.05811 17.3744 1.05811C11.3215 1.05811 7.31492 1.27681 4.75073 2.40571C2.12183 3.56033 1 5.67018 1 9.46533C1 11.3854 1.47462 12.8392 2.44852 13.9102C3.14504 14.6113 4.15284 15.1034 5.72463 15.5118C5.74929 15.5183 8.45216 16.1615 13.035 16.5539C13.2692 16.5732 13.5343 16.5989 13.8363 16.6279C14.6777 16.7051 15.8334 16.8144 17.4114 16.9238C18.4377 16.9945 19.3284 17.0331 20.1143 17.0653C20.8539 17.0974 21.4919 17.1232 22.0035 17.1682C22.1237 17.1811 22.2655 17.1907 22.4226 17.2036C24.0777 17.3322 25.708 17.5123 25.7234 18.1749C25.7357 18.6798 25.4707 19.2202 24.1177 19.397C22.9312 19.5546 22.3795 19.6093 20.8416 19.6093C19.0572 19.6093 14.3387 19.4614 13.2446 19.2169C12.7052 19.0979 12.3138 18.9596 12.0118 18.786C11.7005 18.6059 11.4725 18.3646 11.3492 18.0848H1.38833V18.3807H1.40373L1.40682 18.4322C1.69344 25.138 5.66915 26.833 19.1311 26.833Z" fill="white"/>
<text opacity="0.6" fill="white" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="10" font-weight="bold" letter-spacing="0em"><tspan x="282" y="24.9668">BugBounty Rating:</tspan></text>
<text fill="#88F000" xml:space="preserve" style="white-space: pre" font-family="TT Norms Pro" font-size="30" font-weight="bold" letter-spacing="0em"><tspan x="380.922" y="27">{bbPosition}</tspan></text>
<rect x="1" y="45" width="274" height="129" rx="10" fill="url(#paint0_linear_65_3326)"/>
<text opacity="0.6" fill="white" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="10" font-weight="bold" letter-spacing="0em"><tspan x="11" y="65.4668">Username:  </tspan></text>
<text fill="#00FFA6" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="12" font-weight="bold" letter-spacing="0em"><tspan x="198.906" y="66.1602">{username}</tspan></text>
<text opacity="0.6" fill="white" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="10" font-weight="bold" letter-spacing="0em"><tspan x="11" y="84.4668">Reports quality:</tspan></text>
<text fill="#00FFA6" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="12" font-weight="bold" letter-spacing="0em"><tspan x="220.938" y="85.1602">{signal}</tspan></text>
<text opacity="0.6" fill="white" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="10" font-weight="bold" letter-spacing="0em"><tspan x="11" y="103.467">Reports impact:</tspan></text>
<text fill="#00FFA6" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="12" font-weight="bold" letter-spacing="0em"><tspan x="216.941" y="104.16">{impact}</tspan></text>
<text opacity="0.6" fill="white" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="10" font-weight="bold" letter-spacing="0em"><tspan x="11" y="122.467">Total report count:</tspan></text>
<text fill="#00FFA6" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="12" font-weight="bold" letter-spacing="0em"><tspan x="160.926" y="123.16">{reportsTotal}</tspan></text>
<text opacity="0.6" fill="white" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="10" font-weight="bold" letter-spacing="0em"><tspan x="11" y="141.467">Reports finished:</tspan></text>
<text fill="#00FFA6" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="12" font-weight="bold" letter-spacing="0em"><tspan x="164.887" y="142.16">{reportsFinished}</tspan></text>
<text opacity="0.6" fill="white" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="10" font-weight="bold" letter-spacing="0em"><tspan x="11" y="160.467">Reports in progress:</tspan></text>
<text fill="#00FFA6" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="12" font-weight="bold" letter-spacing="0em"><tspan x="151.527" y="161.16">{reportsInProgress}</tspan></text>
<rect x="282" y="45" width="274" height="129" rx="10" fill="url(#paint1_linear_65_3326)"/>
<text opacity="0.6" fill="white" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="10" font-weight="bold" letter-spacing="0em"><tspan x="292" y="65.4668">Accepted reports:</tspan></text>
<text fill="#00FFA6" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="12" font-weight="bold" letter-spacing="0em"><tspan x="441.211" y="66.1602">{reportsAccepted}</tspan></text>
<text opacity="0.6" fill="white" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="10" font-weight="bold" letter-spacing="0em"><tspan x="292" y="84.4668">Informational:</tspan></text>
<text fill="#00FFA6" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="12" font-weight="bold" letter-spacing="0em"><tspan x="419.203" y="85.1602">{reportsInformational}</tspan></text>
<text opacity="0.6" fill="white" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="10" font-weight="bold" letter-spacing="0em"><tspan x="292" y="103.467">Duplicate:</tspan></text>
<text fill="#00FFA6" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="12" font-weight="bold" letter-spacing="0em"><tspan x="441.211" y="104.16">{reportsDuplicate}</tspan></text>
<text opacity="0.6" fill="white" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="10" font-weight="bold" letter-spacing="0em"><tspan x="292" y="122.467">Out of scope:</tspan></text>
<text fill="#00FFA6" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="12" font-weight="bold" letter-spacing="0em"><tspan x="425.227" y="123.16">{reportsOutOfScope}</tspan></text>
<text opacity="0.6" fill="white" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="10" font-weight="bold" letter-spacing="0em"><tspan x="292" y="141.467">Rejected:</tspan></text>
<text fill="#00FFA6" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="12" font-weight="bold" letter-spacing="0em"><tspan x="445.207" y="142.16">{reportsRejected}</tspan></text>
<text opacity="0.6" fill="white" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="10" font-weight="bold" letter-spacing="0em"><tspan x="292" y="160.467">Spam:</tspan></text>
<text fill="#00FFA6" xml:space="preserve" style="white-space: pre" font-family="Arial" font-size="12" font-weight="bold" letter-spacing="0em"><tspan x="458.566" y="161.16">{reportsAbuse}</tspan></text>
<defs>
<linearGradient id="paint0_linear_65_3326" x1="27.5504" y1="45" x2="120.576" y2="250.313" gradientUnits="userSpaceOnUse">
<stop stop-color="#251548"/>
<stop offset="1" stop-color="#160611"/>
</linearGradient>
<linearGradient id="paint1_linear_65_3326" x1="308.55" y1="45" x2="401.576" y2="250.313" gradientUnits="userSpaceOnUse">
<stop stop-color="#251548"/>
<stop offset="1" stop-color="#160611"/>
</linearGradient>
</defs>
</svg>

    '''
    return bbsvg_template
