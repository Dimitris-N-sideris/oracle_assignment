import unittest
from oracle_assignment import create_df, top_10_requests, percentage_success_requests, percentage_failed_requests, top_10_failed_requests, top_10_hosts, top_10_hosts_with_top_requests

testing_file_location = '../testing_files/small_test_log.txt'


class basic_Test(unittest.TestCase):
    def setUp(self):
        self.df = create_df(testing_file_location)
    

    def test_top_10_requests(self):
        actual = top_10_requests(self.df)
        print(actual)
        expected = """                                              request  # requests
17              GET /images/ksclogosmall.gif HTTP/1.0           7
32  GET /shuttle/resources/orbiters/orbiters-logo....           5
6                   GET /history/history.htm HTTP/1.0           4
11             GET /images/KSC-logosmall.gif HTTP/1.0           3
18               GET /images/launch-logo.gif HTTP/1.0           3
5   GET /history/apollo/images/apollo-logo1.gif HT...           3
13            GET /images/NASA-logosmall.gif HTTP/1.0           3
1   GET /cgi-bin/imagemap/countdown70?285,291 HTTP...           2
15           GET /images/WORLD-logosmall.gif HTTP/1.0           2
14             GET /images/USA-logosmall.gif HTTP/1.0           2
"""
        self.assertEqual(
            actual,
            expected,
            'Expected: top 10 requests',
        )
    
    def test_percentage_success_requests(self):
        actual = percentage_success_requests(self.df)
        expected = "Successful Requests percentage: 83.33 %\n"
        print(actual)
        self.assertEqual(
            actual,
            expected,
            'Expected:  Successful Requests percentage: 83.33 %',
        )



    def test_percentage_failed_requests(self):
        actual = percentage_failed_requests(self.df)
        print(actual)
        expected = "Failed Requests percentage: 16.67 %\n"
        self.assertEqual(
            actual,
            expected,
            'Expected: Failed Requests percentage: 16.67 %',
        )



    def test_top_10_failed_requests(self):
        actual = top_10_failed_requests(self.df)
        print(actual)
        expected = """                                             request  # requests
1                  GET /history/history.htm HTTP/1.0           4
2              GET /images/ksclogosmall.gif HTTP/1.0           3
3  GET /shuttle/resources/orbiters/orbiters-logo....           2
0  GET /cgi-bin/imagemap/countdown70?285,291 HTTP...           1\n"""
        self.assertEqual(
            actual,
            expected,
            'Expected: top 10 failed requests',
        )



    def test_top_10_hosts(self):
        actual = top_10_hosts(self.df)
        print(actual)
        expected = """                           host  # requests
8               uplherc.upl.com          20
0                  133.43.96.45           8
3   ix-esc-ca2-07.ix.netcom.com           6
4    kgtyk4.kj.yamagata-u.ac.jp           6
7          slppp6.intermind.net           6
5  miriworld.its.unimelb.edu.au           4
6          piweba4y.prodigy.com           3
1               d0ucr6.fnal.gov           2
2             in24.inetnebr.com           2
9          www-c3.proxy.aol.com           2\n"""
        self.assertEqual(
            actual,
            expected,
            'Expected: top 10 hosts',
        )



    def test_top_10_hosts_with_top_requests(self):
        actual = top_10_hosts_with_top_requests(self.df)
        print(actual)
        expected = """Host: uplherc.upl.com 
                                              request  # requests
8               GET /images/ksclogosmall.gif HTTP/1.0           4
14  GET /shuttle/resources/orbiters/orbiters-logo....           3
0                                      GET / HTTP/1.0           1
1   GET /history/apollo/images/apollo-logo1.gif HT...           1
2              GET /images/KSC-logosmall.gif HTTP/1.0           1
Host: 133.43.96.45 
                                             request  # requests
0  GET /history/apollo/images/apollo-logo1.gif HT...           1
1             GET /images/KSC-logosmall.gif HTTP/1.0           1
2              GET /images/ksclogosmall.gif HTTP/1.0           1
3               GET /images/launch-logo.gif HTTP/1.0           1
4  GET /shuttle/missions/sts-69/mission-sts-69.ht...           1
Host: ix-esc-ca2-07.ix.netcom.com 
                                             request  # requests
0  GET /history/apollo/images/apollo-logo1.gif HT...           1
1              GET /images/ksclogosmall.gif HTTP/1.0           1
2               GET /images/launch-logo.gif HTTP/1.0           1
3  GET /shuttle/resources/orbiters/discovery-logo...           1
4  GET /shuttle/resources/orbiters/discovery.html...           1
Host: kgtyk4.kj.yamagata-u.ac.jp 
                                     request  # requests
0                             GET / HTTP/1.0           1
1  GET /images/MOSAIC-logosmall.gif HTTP/1.0           1
2    GET /images/NASA-logosmall.gif HTTP/1.0           1
3     GET /images/USA-logosmall.gif HTTP/1.0           1
4   GET /images/WORLD-logosmall.gif HTTP/1.0           1
Host: slppp6.intermind.net 
                                             request  # requests
0  GET /history/apollo/images/apollo-logo.gif HTT...           1
1         GET /history/skylab/skylab-1.html HTTP/1.0           1
2       GET /history/skylab/skylab-logo.gif HTTP/1.0           1
3      GET /history/skylab/skylab-small.gif HTTP/1.0           1
4           GET /history/skylab/skylab.html HTTP/1.0           1
Host: miriworld.its.unimelb.edu.au 
                             request  # requests
0  GET /history/history.htm HTTP/1.0           4
Host: piweba4y.prodigy.com 
                                   request  # requests
0   GET /images/KSC-logosmall.gif HTTP/1.0           1
1  GET /images/NASA-logosmall.gif HTTP/1.0           1
2    GET /images/launchmedium.gif HTTP/1.0           1
Host: d0ucr6.fnal.gov 
                                             request  # requests
0  GET /history/apollo/apollo-16/apollo-16-patch-...           1
1  GET /history/apollo/apollo-16/apollo-16.html H...           1
Host: in24.inetnebr.com 
                                             request  # requests
0  GET /shuttle/missions/sts-68/news/sts-68-mcc-0...           1
1  GET /shuttle/missions/sts-68/news/sts-68-mcc-0...           1
Host: www-c3.proxy.aol.com 
                                             request  # requests
0  GET /cgi-bin/imagemap/countdown70?285,291 HTTP...           2
"""
        self.assertEqual(
            actual,
            expected,
            'Expected: top 10 hosts and their top 5 requests',
        )





if __name__ == "__main__":
    unittest.main(module='test_main')