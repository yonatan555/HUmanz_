#read csv
import requests
import time
data =  [
        {
            "fullName": "Name",
            "id": "ID",
            "phoneNumber": "IP",
            "ipAddress": "Phone"
        },
        {
            "fullName": "Priscilla Matthews",
            "id": "384525101",
            "phoneNumber": "80.119.117.187",
            "ipAddress": "+972-523862672"
        },
        {
            "fullName": "Benjamin Douglas",
            "id": "660652470",
            "phoneNumber": "104.29.98.222",
            "ipAddress": "+972-557712987"
        },
        {
            "fullName": "Jordan Porter",
            "id": "753184050",
            "phoneNumber": "1.10.243.200",
            "ipAddress": "+972-532509246"
        },
        {
            "fullName": "Jacqueline Hughes",
            "id": "875322869",
            "phoneNumber": "103.255.178.143",
            "ipAddress": "+972-551448824"
        },
        {
            "fullName": "Max Dunn",
            "id": "338605579",
            "phoneNumber": "88.144.81.24",
            "ipAddress": "+972-543503816"
        },
        {
            "fullName": "Christy Neal",
            "id": "068672047",
            "phoneNumber": "62.113.223.73",
            "ipAddress": "+972-542202337"
        },
        {
            "fullName": "Jessica Rodriquez",
            "id": "150318228",
            "phoneNumber": "12.189.93.218",
            "ipAddress": "+972-558975263"
        },
        {
            "fullName": "Terri Gordon",
            "id": "482018827",
            "phoneNumber": "212.74.99.171",
            "ipAddress": "+972-505375808"
        },
        {
            "fullName": "Frank Hamilton",
            "id": "790979272",
            "phoneNumber": "70.32.16.194",
            "ipAddress": "+972-541414650"
        },
        {
            "fullName": "Felecia Ford",
            "id": "534268339",
            "phoneNumber": "77.139.213.201",
            "ipAddress": "+972-559328061"
        },
        {
            "fullName": "Aubree Long",
            "id": "039512322",
            "phoneNumber": "121.113.29.210",
            "ipAddress": "+972-507896703"
        },
        {
            "fullName": "Tristan Brewer",
            "id": "091900407",
            "phoneNumber": "50.87.175.194",
            "ipAddress": "+972-545165250"
        },
        {
            "fullName": "Mattie Ross",
            "id": "403769532",
            "phoneNumber": "94.252.132.224",
            "ipAddress": "+972-534831657"
        },
        {
            "fullName": "Miriam Caldwell",
            "id": "767862527",
            "phoneNumber": "105.168.58.247",
            "ipAddress": "+972-542739332"
        },
        {
            "fullName": "Dolores Robertson",
            "id": "068576123",
            "phoneNumber": "139.228.93.215",
            "ipAddress": "+972-545560916"
        },
        {
            "fullName": "Christina Hunt",
            "id": "470236670",
            "phoneNumber": "75.128.159.27",
            "ipAddress": "+972-549627649"
        },
        {
            "fullName": "Ethel Freeman",
            "id": "451148183",
            "phoneNumber": "198.55.114.244",
            "ipAddress": "+972-535050005"
        },
        {
            "fullName": "Marilyn Kelley",
            "id": "127141687",
            "phoneNumber": "109.122.224.164",
            "ipAddress": "+972-523314497"
        },
        {
            "fullName": "Marvin Kim",
            "id": "969423987",
            "phoneNumber": "86.140.236.36",
            "ipAddress": "+972-543576817"
        },
        {
            "fullName": "Monica Shelton",
            "id": "008736928",
            "phoneNumber": "113.185.43.99",
            "ipAddress": "+972-541350820"
        },
        {
            "fullName": "Flenn Neal",
            "id": "938993938",
            "phoneNumber": "207.171.162.115",
            "ipAddress": "+972-530574010"
        },
        {
            "fullName": "Timmothy Riley",
            "id": "366232932",
            "phoneNumber": "71.69.19.61",
            "ipAddress": "+972-548714955"
        },
        {
            "fullName": "Gladys Gomez",
            "id": "224058453",
            "phoneNumber": "62.221.151.150",
            "ipAddress": "+972-553118725"
        },
        {
            "fullName": "Ray Ortiz",
            "id": "140198631",
            "phoneNumber": "123.139.35.70",
            "ipAddress": "+972-501371777"
        },
        {
            "fullName": "Mike White",
            "id": "043993278",
            "phoneNumber": "197.253.220.3",
            "ipAddress": "+972-541117565"
        },
        {
            "fullName": "Terri Byrd",
            "id": "624213302",
            "phoneNumber": "170.79.229.235",
            "ipAddress": "+972-552658624"
        },
        {
            "fullName": "Joyce Duncan",
            "id": "760444406",
            "phoneNumber": "104.237.52.50",
            "ipAddress": "+972-524138666"
        },
        {
            "fullName": "Carole Garrett",
            "id": "133292698",
            "phoneNumber": "106.10.73.22",
            "ipAddress": "+972-523988066"
        },
        {
            "fullName": "Joan Jackson",
            "id": "976579458",
            "phoneNumber": "24.66.90.83",
            "ipAddress": "+972-552037957"
        },
        {
            "fullName": "Mark Black",
            "id": "622795052",
            "phoneNumber": "191.6.137.31",
            "ipAddress": "+972-537608013"
        },
        {
            "fullName": "Eugene Frazier",
            "id": "826328668",
            "phoneNumber": "216.208.233.155",
            "ipAddress": "+972-544545920"
        },
        {
            "fullName": "Terry Carr",
            "id": "222487571",
            "phoneNumber": "103.19.16.90",
            "ipAddress": "+972-527662962"
        },
        {
            "fullName": "Samuel Murray",
            "id": "562368886",
            "phoneNumber": "8.40.166.238",
            "ipAddress": "+972-505707479"
        },
        {
            "fullName": "Donald May",
            "id": "201431194",
            "phoneNumber": "187.94.129.66",
            "ipAddress": "+972-558091299"
        },
        {
            "fullName": "Claude Woods",
            "id": "637163908",
            "phoneNumber": "78.170.254.42",
            "ipAddress": "+972-537094406"
        },
        {
            "fullName": "Alan Steward",
            "id": "631615440",
            "phoneNumber": "186.210.91.59",
            "ipAddress": "+972-541849674"
        },
        {
            "fullName": "Christina Dean",
            "id": "379978463",
            "phoneNumber": "156.210.111.98",
            "ipAddress": "+972-521882261"
        },
        {
            "fullName": "Maurice Boyd",
            "id": "871700894",
            "phoneNumber": "151.250.232.140",
            "ipAddress": "+972-534230979"
        },
        {
            "fullName": "Daryl Mason",
            "id": "596921817",
            "phoneNumber": "104.218.66.37",
            "ipAddress": "+972-548206508"
        },
        {
            "fullName": "Alyssa Stephens",
            "id": "139193023",
            "phoneNumber": "109.74.13.84",
            "ipAddress": "+972-544077527"
        },
        {
            "fullName": "Stanley Rivera",
            "id": "432787646",
            "phoneNumber": "195.184.106.3",
            "ipAddress": "+972-536586531"
        },
        {
            "fullName": "Bill Mitchelle",
            "id": "353546336",
            "phoneNumber": "209.58.169.183",
            "ipAddress": "+972-520280447"
        },
        {
            "fullName": "Diana Peck",
            "id": "477398853",
            "phoneNumber": "13.225.189.253",
            "ipAddress": "+972-541500479"
        },
        {
            "fullName": "Owen Pearson",
            "id": "429480874",
            "phoneNumber": "190.205.100.27",
            "ipAddress": "+972-542685335"
        },
        {
            "fullName": "Alan Wheeler",
            "id": "021630314",
            "phoneNumber": "185.5.17.140",
            "ipAddress": "+972-526012379"
        },
        {
            "fullName": "Theresa Griffin",
            "id": "991133273",
            "phoneNumber": "184.162.191.22",
            "ipAddress": "+972-532713164"
        },
        {
            "fullName": "Dwayne Allen",
            "id": "840694103",
            "phoneNumber": "80.119.117.49",
            "ipAddress": "+972-551937240"
        },
        {
            "fullName": "Franklin Phillips",
            "id": "870256526",
            "phoneNumber": "130.185.144.76",
            "ipAddress": "+972-509060787"
        },
        {
            "fullName": "Greg Medina",
            "id": "018169151",
            "phoneNumber": "104.20.218.249",
            "ipAddress": "+972-508112956"
        },
        {
            "fullName": "Kirk Fuller",
            "id": "545884686",
            "phoneNumber": "108.62.122.143",
            "ipAddress": "+972-555611424"
        }
    
    ]


url = 'http://localhost:3000/api/client/add'
for jsn in data:
    requests.post(url, json=jsn)
    time.sleep(3)







