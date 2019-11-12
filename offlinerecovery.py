import subprocess

subprocess.call(['bash -c "sudo chmod +x ~/yetirecovery/dpkg-script.sh; sudo ~/yetirecovery/dpkg-script.sh"'],shell=True)
subprocess.call(['sudo chmod +x ~/yetirecovery/bitcoin-0.19.0rc1/bin/bitcoin-cli'],shell=True)
subprocess.call(['sudo chmod +x ~/yetirecovery/bitcoin-0.19.0rc1/bin/bitcoind'],shell=True)
subprocess.call(['sudo chmod +x ~/yetirecovery/bitcoin-0.19.0rc1/bin/bitcoin-qt'],shell=True)
subprocess.call(['sudo chmod +x ~/yetirecovery/bitcoin-0.19.0rc1/bin/bitcoin-wallet'],shell=True)
subprocess.call(['sudo chmod +x ~/yetirecovery/bitcoin-0.19.0rc1/bin/bitcoin-tx'],shell=True)
subprocess.Popen('python3 ~/yetirecovery/hello.py',shell=True,start_new_session=True)
subprocess.call(['xdg-open http://localhost:5000/step11'],shell=True)
