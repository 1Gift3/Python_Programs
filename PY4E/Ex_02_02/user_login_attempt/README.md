
# WHAT
# Max_attempts acts as a max attempt where the user is allowed to try to log in certain number of times before being locked out temporarily
# Lock_time checks if the users exceeds the max number of login attempts(max_attempts), which will temorarily lockout for a specified period which is set to 10 ses and during this time you cant attempt to log in
# Then the program keeps track of number of incorrect attempts and enforeces the limit on failed logins.

# HOW
# Can be used to prevent brute force attacks 
# By limiting attempts after a certain number of failed login attempts, where the system temporarily locks the user out.
# Delaying between attempts enforcing delay (time.spleep()) between repeated login attempts forces attackers to  wait, slowing down brute force attempts significantly.

# WHY
# Can be used to protect user accounts fro Unauthorized access
# Redusing risk of account compromise
# Mitigating distributed attacks
# Preventing automated attacks
# Ensurinfg fair access and reducing system load
# encouraging strong passwords
# improving user trust
