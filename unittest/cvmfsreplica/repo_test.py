#/usr/bin/python

import unittest
from mock import Mock, patch

from cvmfsreplica.replicas import Repository

class TestDate2Seconds(unittest.TestCase):

    #@patch('cvmfsreplica.replicas.Repository')
    #def test_create_repository_object(self, mock_requests):
        #mock_requests._get_cvmfs_config.return_value = None
        #mock_requests._readreportplugins.return_value = None
        #mock_requests._readacceptanceplugins.return_value = None
        #mock_requests._readpostplugins.return_value = None
        #mock_requests._get_cvmfs_upstream_storage.return_value = 'abc'
        #mock_requests._snapshotdate.return_value = 123

    @patch('cvmfsreplica.replicas.Repository._get_cvmfs_config')
    @patch('cvmfsreplica.replicas.Repository._readreportplugins')
    @patch('cvmfsreplica.replicas.Repository._readacceptanceplugins')
    @patch('cvmfsreplica.replicas.Repository._readpostplugins')
    @patch('cvmfsreplica.replicas.Repository._get_cvmfs_upstream_storage')
    @patch('cvmfsreplica.replicas.Repository._snapshotdate')
    def test_create_repository_object(self, m1, m2, m3, m4, m5, m6):
        m1.return_value = None
        m2.return_value = None
        m3.return_value = None
        m4.return_value = None
        m5.return_value = 'abc'
        m6.return_value = 123 

        
        m = Mock()
        repo = Repository(m, m, m)


if __name__ == '__main__':
    unittest.main()

