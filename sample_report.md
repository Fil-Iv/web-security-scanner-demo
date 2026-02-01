# Demo Security Report

Target: https://example.com

## Findings

### Missing Content-Security-Policy
**Risk:** Medium  
**Description:** The site does not define a CSP header.  
**Recommendation:** Add a restrictive CSP policy.

### Cookies detected
**Risk:** Low  
**Description:** Cookies were detected without deep flag analysis (demo limitation).
