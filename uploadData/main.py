#read csv
import requests
import time
data = [
 {
   'fullName': 'Priscilla Matthews',
   'id': 384525101,
   'ipAddress': '80.119.117.187',
   'phoneNumber': '+972-523862672'
 },
 {
   'fullName': 'Benjamin Douglas',
   'id': 660652470,
   'ipAddress': '104.29.98.222',
   'phoneNumber': '+972-557712987'
 },
 {
   'fullName': 'Jordan Porter',
   'id': 753184050,
   'ipAddress': '1.10.243.200',
   'phoneNumber': '+972-532509246'
 },
 {
   'fullName': 'Jacqueline Hughes',
   'id': 875322869,
   'ipAddress': '103.255.178.143',
   'phoneNumber': '+972-551448824'
 },
 {
   'fullName': 'Max Dunn',
   'id': 338605579,
   'ipAddress': '88.144.81.24',
   'phoneNumber': '+972-543503816'
 },
 {
   'fullName': 'Christy Neal',
   'id': 68672047,
   'ipAddress': '62.113.223.73',
   'phoneNumber': '+972-542202337'
 },
 {
   'fullName': 'Jessica Rodriquez',
   'id': 150318228,
   'ipAddress': '12.189.93.218',
   'phoneNumber': '+972-558975263'
 },
 {
   'fullName': 'Terri Gordon',
   'id': 482018827,
   'ipAddress': '212.74.99.171',
   'phoneNumber': '+972-505375808'
 },
 {
   'fullName': 'Frank Hamilton',
   'id': 790979272,
   'ipAddress': '70.32.16.194',
   'phoneNumber': '+972-541414650'
 },
 {
   'fullName': 'Felecia Ford',
   'id': 534268339,
   'ipAddress': '77.139.213.201',
   'phoneNumber': '+972-559328061'
 },
 {
   'fullName': 'Aubree Long',
   'id': 39512322,
   'ipAddress': '121.113.29.210',
   'phoneNumber': '+972-507896703'
 },
 {
   'fullName': 'Tristan Brewer',
   'id': 91900407,
   'ipAddress': '50.87.175.194',
   'phoneNumber': '+972-545165250'
 },
 {
   'fullName': 'Mattie Ross',
   'id': 403769532,
   'ipAddress': '94.252.132.224',
   'phoneNumber': '+972-534831657'
 },
 {
   'fullName': 'Miriam Caldwell',
   'id': 767862527,
   'ipAddress': '105.168.58.247',
   'phoneNumber': '+972-542739332'
 },
 {
   'fullName': 'Dolores Robertson',
   'id': 68576123,
   'ipAddress': '139.228.93.215',
   'phoneNumber': '+972-545560916'
 },
 {
   'fullName': 'Christina Hunt',
   'id': 470236670,
   'ipAddress': '75.128.159.27',
   'phoneNumber': '+972-549627649'
 },
 {
   'fullName': 'Ethel Freeman',
   'id': 451148183,
   'ipAddress': '198.55.114.244',
   'phoneNumber': '+972-535050005'
 },
 {
   'fullName': 'Marilyn Kelley',
   'id': 127141687,
   'ipAddress': '109.122.224.164',
   'phoneNumber': '+972-523314497'
 },
 {
   'fullName': 'Marvin Kim',
   'id': 969423987,
   'ipAddress': '86.140.236.36',
   'phoneNumber': '+972-543576817'
 },
 {
   'fullName': 'Monica Shelton',
   'id': 8736928,
   'ipAddress': '113.185.43.99',
   'phoneNumber': '+972-541350820'
 },
 {
   'fullName': 'Flenn Neal',
   'id': 938993938,
   'ipAddress': '207.171.162.115',
   'phoneNumber': '+972-530574010'
 },
 {
   'fullName': 'Timmothy Riley',
   'id': 366232932,
   'ipAddress': '71.69.19.61',
   'phoneNumber': '+972-548714955'
 },
 {
   'fullName': 'Gladys Gomez',
   'id': 224058453,
   'ipAddress': '62.221.151.150',
   'phoneNumber': '+972-553118725'
 },
 {
   'fullName': 'Ray Ortiz',
   'id': 140198631,
   'ipAddress': '123.139.35.70',
   'phoneNumber': '+972-501371777'
 },
 {
   'fullName': 'Mike White',
   'id': 43993278,
   'ipAddress': '197.253.220.3',
   'phoneNumber': '+972-541117565'
 },
 {
   'fullName': 'Terri Byrd',
   'id': 624213302,
   'ipAddress': '170.79.229.235',
   'phoneNumber': '+972-552658624'
 },
 {
   'fullName': 'Joyce Duncan',
   'id': 760444406,
   'ipAddress': '104.237.52.50',
   'phoneNumber': '+972-524138666'
 },
 {
   'fullName': 'Carole Garrett',
   'id': 133292698,
   'ipAddress': '106.10.73.22',
   'phoneNumber': '+972-523988066'
 },
 {
   'fullName': 'Joan Jackson',
   'id': 976579458,
   'ipAddress': '24.66.90.83',
   'phoneNumber': '+972-552037957'
 },
 {
   'fullName': 'Mark Black',
   'id': 622795052,
   'ipAddress': '191.6.137.31',
   'phoneNumber': '+972-537608013'
 },
 {
   'fullName': 'Eugene Frazier',
   'id': 826328668,
   'ipAddress': '216.208.233.155',
   'phoneNumber': '+972-544545920'
 },
 {
   'fullName': 'Terry Carr',
   'id': 222487571,
   'ipAddress': '103.19.16.90',
   'phoneNumber': '+972-527662962'
 },
 {
   'fullName': 'Samuel Murray',
   'id': 562368886,
   'ipAddress': '8.40.166.238',
   'phoneNumber': '+972-505707479'
 },
 {
   'fullName': 'Donald May',
   'id': 201431194,
   'ipAddress': '187.94.129.66',
   'phoneNumber': '+972-558091299'
 },
 {
   'fullName': 'Claude Woods',
   'id': 637163908,
   'ipAddress': '78.170.254.42',
   'phoneNumber': '+972-537094406'
 },
 {
   'fullName': 'Alan Steward',
   'id': 631615440,
   'ipAddress': '186.210.91.59',
   'phoneNumber': '+972-541849674'
 },
 {
   'fullName': 'Christina Dean',
   'id': 379978463,
   'ipAddress': '156.210.111.98',
   'phoneNumber': '+972-521882261'
 },
 {
   'fullName': 'Maurice Boyd',
   'id': 871700894,
   'ipAddress': '151.250.232.140',
   'phoneNumber': '+972-534230979'
 },
 {
   'fullName': 'Daryl Mason',
   'id': 596921817,
   'ipAddress': '104.218.66.37',
   'phoneNumber': '+972-548206508'
 },
 {
   'fullName': 'Alyssa Stephens',
   'id': 139193023,
   'ipAddress': '109.74.13.84',
   'phoneNumber': '+972-544077527'
 },
 {
   'fullName': 'Stanley Rivera',
   'id': 432787646,
   'ipAddress': '195.184.106.3',
   'phoneNumber': '+972-536586531'
 },
 {
   'fullName': 'Bill Mitchelle',
   'id': 353546336,
   'ipAddress': '209.58.169.183',
   'phoneNumber': '+972-520280447'
 },
 {
   'fullName': 'Diana Peck',
   'id': 477398853,
   'ipAddress': '13.225.189.253',
   'phoneNumber': '+972-541500479'
 },
 {
   'fullName': 'Owen Pearson',
   'id': 429480874,
   'ipAddress': '190.205.100.27',
   'phoneNumber': '+972-542685335'
 },
 {
   'fullName': 'Alan Wheeler',
   'id': 21630314,
   'ipAddress': '185.5.17.140',
   'phoneNumber': '+972-526012379'
 },
 {
   'fullName': 'Theresa Griffin',
   'id': 991133273,
   'ipAddress': '184.162.191.22',
   'phoneNumber': '+972-532713164'
 },
{
   'fullName': 'Dwayne Allen',
   'id': 840694103,
   'ipAddress': '80.119.117.49',
   'phoneNumber': '+972-551937240'
 },
 {
   'fullName': 'Franklin Phill',
   'id': 870256526,
   'ipAddress': '130.185.144.76',
   'phoneNumber': '+972-509060787'
 },
 {
   'fullName': 'Greg Medina',
   'id': 18169151,
   'ipAddress': '104.20.218.249',
   'phoneNumber': '+972-508112956'
 },
 {
   'fullName': 'Kirk Fuller',
   'id': 545884686,
   'ipAddress': '108.62.122.143',
   'phoneNumber': '+972-555611424'
 }
]


url = 'http://localhost:3000/api/client/add'
for jsn in data:
    requests.post(url, json=jsn)
    time.sleep(3)







