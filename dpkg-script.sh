tar -xzf ToDisconnected.tar.gz
cd ~/dpkg-repack
sudo dpkg -i *.deb
pip3 install -r ~/yetirecovery/reqs.txt --no-index --find-links ~/dpkg-repack/wheelhouse
echo "Done unpackaging. Close this terminal window now."
