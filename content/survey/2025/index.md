---
title: '2025 Survey Assessing Risks from AI'
date: 2025-01-01
type: landing

sections:
  - block: markdown
    content:
      text: |-
        <div id="embargo-overlay" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.95); z-index: 9999; display: flex; align-items: center; justify-content: center;">
          <div style="background: white; padding: 40px; border-radius: 10px; max-width: 500px; text-align: center; color: #000;">
            <h2 style="margin-top: 0; color: #0C869B;">Content Under Embargo</h2>
            <p id="countdown-text" style="font-size: 1.2em; margin: 20px 0; font-weight: 600;"></p>
            <div style="margin: 30px 0;">
              <input type="password" id="embargo-password" placeholder="Enter password"
                style="padding: 10px; font-size: 16px; border: 2px solid #0C869B; border-radius: 5px; width: 100%; max-width: 300px;">
            </div>
            <button onclick="checkPassword()"
              style="background: #0C869B; color: white; border: none; padding: 12px 30px; font-size: 16px; border-radius: 5px; cursor: pointer; font-weight: 600;">
              Access Report
            </button>
            <p id="error-message" style="color: red; margin-top: 15px; display: none;">Incorrect password</p>
          </div>
        </div>

        <script>
          // Embargo date: November 27, 2025 at 00:00 AEDT (UTC+11)
          const embargoDate = new Date('2025-11-27T00:00:00+11:00');

          // Simple password (change this to whatever you want)
          const correctPasswordHash = 'SARA2025'; // Change this password

          function checkPassword() {
            const input = document.getElementById('embargo-password').value;
            if (input === correctPasswordHash) {
              document.getElementById('embargo-overlay').style.display = 'none';
              sessionStorage.setItem('sara2025-access', 'granted');
            } else {
              document.getElementById('error-message').style.display = 'block';
            }
          }

          // Allow Enter key to submit
          document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('embargo-password').addEventListener('keypress', function(e) {
              if (e.key === 'Enter') {
                checkPassword();
              }
            });

            // Check if already authenticated in this session
            if (sessionStorage.getItem('sara2025-access') === 'granted') {
              document.getElementById('embargo-overlay').style.display = 'none';
            }

            updateCountdown();
          });

          function updateCountdown() {
            const now = new Date();
            const timeLeft = embargoDate - now;

            // If embargo has passed, hide overlay
            if (timeLeft <= 0) {
              document.getElementById('embargo-overlay').style.display = 'none';
              return;
            }

            // Calculate days, hours, minutes
            const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
            const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));

            document.getElementById('countdown-text').innerHTML =
              `Embargo lifts in:<br><strong style="font-size: 1.5em; color: #0C869B;">${days}d ${hours}h ${minutes}m</strong><br><small>November 27, 2025</small>`;

            // Update every minute
            setTimeout(updateCountdown, 60000);
          }
        </script>
    design:
      columns: '1'

  - block: hero
    content:
      title: |-
        Survey Assessing Risks from AI 2025
      image:
        filename: hero2025.png
      text: |-
        Understanding Australian public views on AI risks and governance
        
        We conducted a representative survey of 933 Australian adults to understand public perceptions of AI risks and support for AI governance actions in Australia.
        

      cta:
        label: View Report
        url: '/survey/2025/sara_2025_technical_report.html'
        icon_pack: fas
        icon: star
      cta_alt:
        label: See 2024
        url: '/survey/2024/'
    design:
      background:
        color: #0C869B

  - block: markdown
    content:
      title: Key Insights
      text: |-
        > **Comparing surveys:** View [2024 findings](/survey/2024/)

        **2025 Survey** (933 Australians): Australians expect AI to be as safe as commercial aviation - at least **4,000x** safer than current risk estimates. They want the government to better manage AI risks, and many risk controls would increase their trust in AI.

    design:
      columns: '2'

  - block: markdown
    content:
      title: What This Means for Australia
      text: |-
        **Safety standards matter**: Australians hold AI to the same rigorous safety standards as commercial aviation. This means they expect AI systems to cause fewer than 1 death per 100 million hours of operation—far stricter than current AI safety benchmarks.

        **Public trust depends on action**: The research shows that implementing appropriate risk controls would directly increase trust in AI technology. This presents a clear pathway for both government and industry.

        **Governance framework needed**: With strong public support for government action on AI risks, there is a mandate for developing comprehensive AI governance frameworks that address current harms and potential catastrophic risks.

    design:
      columns: '2'

  - block: markdown
    content:
      title: How to Read This Research
      text: |-
        - [2025 Technical Report](/survey/2025/sara_2025_technical_report.html) (interactive report) - Complete findings, read online
        - [2025 Technical Report](/survey/2025/sara_2025_technical_report_final.pdf) (PDF) - Complete report for download and offline reading

        **Suggested citation:** Noetel, M., Saeri, A.K., Graham, J., & Slattery, P. (2025). *Survey Assessing Risks from Artificial Intelligence: 2025 Technical Report*. aigovernance.org.au

    design:
      columns: '2'

  - block: markdown
    content:
      title: How We Conducted This Survey
      text: |-

        We analysed data from 933 Australians recruited through online representative quota sampling stratified by age, sex, and Australian state / territory. We also conducted multilevel regression with poststratification to construct more accurate population estimates based on 2021 Australian Census data.

        This project is a collaboration between Ready Research and The University of Queensland. The project team includes [Dr Alexander Saeri](https://www.linkedin.com/in/aksaeri/), [Dr Michael Noetel](https://www.linkedin.com/in/mnoetel/), [Jessica Graham](https://www.linkedin.com/in/jessica-jane-graham/), and [Dr Peter Slattery](https://www.linkedin.com/in/peterslattery1/).

    design:
      columns: '2'

  - block: contact
    id: contact
    content:
      title: Contact
      subtitle: ''
      text: |-
        Contact [Dr Alexander Saeri](mailto:a.saeri@uq.edu.au) to discuss the research project.

        <br>
        <br>
        <img src='/readyuqlogo.png' alt='Ready Research & The University of Queensland logo' style='display: block; margin-right: auto; margin-left: auto;width: 60%' />
      autolink: true
      design:
        columns: '2'
---
