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
   <text x="215" y="41" fill="#88f000" font-size="28" font-weight="bold" font-family="Arial">
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


   <svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" fill="none">
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
           <rect width="220" height="20" y="248" x="10" rx="10" fill="url(#grad)" stroke="#FFFFFF" stroke-width="2"  />
           <rect width="220" height="20" y="268" x="10" rx="10" fill="url(#grad)" stroke="#FFFFFF" stroke-width="2"  />
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
    Username:  </text>
   <text x="25" y="83" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    Reports quality:  </text>
   <text x="25" y="103" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    Reports impact:  </text>
   <text x="25" y="123" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    Tolal report count:  </text>
   <text x="25" y="143" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    Reports finished:  </text>
   <text x="25" y="163" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    Reports in progress:  </text>
   <text x="25" y="183" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    Accepted reports:  </text>
   <text x="25" y="203" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    Informational:  </text>
   <text x="25" y="223" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    Duplicate:  </text>
   <text x="25" y="243" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    Out of scope:  </text>
   <text x="25" y="263" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    Rejected:  </text>
   <text x="25" y="283" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    Spam:  </text>
 <text x="220" y="63" text-anchor="end" fill="#00ffa6" font-size="13" font-weight="bold" font-family="Arial">
  {username}
</text>
 <text x="220" y="83" text-anchor="end" fill="#00ffa6" font-size="13" font-weight="bold" font-family="Arial">
  {signal}
</text>
     
 <text x="220" y="103" text-anchor="end" fill="#00ffa6" font-size="13" font-weight="bold" font-family="Arial">
  {impact}
</text>
 <text x="220" y="123" text-anchor="end" fill="#00ffa6" font-size="13" font-weight="bold" font-family="Arial">
  {reportsTotal}
</text>
 <text x="220" y="143" text-anchor="end" fill="#00ffa6" font-size="13" font-weight="bold" font-family="Arial">
  {reportsFinished}
</text>
 <text x="220" y="163" text-anchor="end" fill="#00ffa6" font-size="13" font-weight="bold" font-family="Arial">
  {reportsInProgress}
</text>
 <text x="220" y="183" text-anchor="end" fill="#00ffa6" font-size="13" font-weight="bold" font-family="Arial">
  {reportsAccepted}
</text>
  <text x="220" y="203" text-anchor="end" fill="#00ffa6" font-size="13" font-weight="bold" font-family="Arial">
  {reportsInformational}
</text>
  <text x="220" y="223" text-anchor="end" fill="#00ffa6" font-size="13" font-weight="bold" font-family="Arial">
  {reportsDuplicate}
</text>
  <text x="220" y="243" text-anchor="end" fill="#00ffa6" font-size="13" font-weight="bold" font-family="Arial">
  {reportsOutOfScope}
</text>
  <text x="220" y="263" text-anchor="end" fill="#00ffa6" font-size="13" font-weight="bold" font-family="Arial">
  {reportsRejected}
</text>
  <text x="220" y="283" text-anchor="end" fill="#00ffa6" font-size="13" font-weight="bold" font-family="Arial">
  {reportsAbuse}
</text>
</svg> 



    '''
    return bbsvg_template