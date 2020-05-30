# I use pycharm to code
#install the package speedtest-cli
#file->settings->project:Tutorials->Project interpreter->(search for speedtest-cli)->install

from speedtest import Speedtest

st = Speedtest()

print("download:",st.download())
print("upload:" ,st.upload())

st.get_servers([])
print("ping :",st.results.ping)