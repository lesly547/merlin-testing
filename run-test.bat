@echo off
IF EXIST reports del /Q reports
CMD /C "behave --junit"
CMD /C "junit2html reports --merge reports/report-test.xml"
CMD /C "junit2html reports/report-test.xml --report-matrix reports/report-test.html"
start "", "reports/report-test.html"