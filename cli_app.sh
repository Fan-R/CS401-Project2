wget --server-response \
 --output-document response.out  \
 --header='Content-Type: application/json'  \
 --post-data '{"text": "#covid19 new york"}' \
 http://10.100.136.180:5002/api/american
 cat response.out