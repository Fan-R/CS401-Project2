# I tested my font end by doing the following on my local computer,
# and it worked for me:
# 
# First I established the SSH tunnel by running the following command:
# ssh -fNT -L 5001:10.100.136.180:5002 rf96@vcm-23691.vm.duke.edu
# 
# Then I can open https://localhost:5001/ on my browser and it works fine.
# 
# Or, I can run the following command in cmd on windows
# start http://localhost:5001/
ssh -fNT -L 5001:10.100.136.180:5002 rf96@vcm-23691.vm.duke.edu
start http://localhost:5001/