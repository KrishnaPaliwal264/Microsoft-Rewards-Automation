## **The Steps To SUccessfully Automate Are --> **

1. CHECK THE COMMAND FOR OPENING A SPECIFIC PROFILE OF MSEDGE💻
  1. Go To MSedge and type 'edge://version' 
  2. Check the command to open the specific profile copy it till for example - C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --profile-directory="Profile 5"
2. ADD THE FOLLOWING PROCESS TO THE ACCOUNT✅
  1. Then edit the command_n variable with that command and add all the prifiles/accounts u want to this (make more variable accordingly)
  2. Go to the end of the program main.py and then add the following subprocess like --> subprocess.run(<span style="color:blue"><u>command_n</u></span>, shell=True)
                                                                                          searches()
                                                                                          time.sleep(5)
                                                                                          activities()
3. PUT ALL THE FILES IN THE RESOPSITORY IN THE SAME DIRECTORY📂
  1. Now replace template_path in activites() function with the path to the template file.
