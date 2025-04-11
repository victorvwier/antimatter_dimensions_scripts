auto infinity 1e+1000 x highest
auto eternity 1e+20 x highest
studies purchase 11-61 62 time 111 active 151-214 72 82 92 102 dark
wait ep >=1e+1200
studies respec
eternity
auto infinity off
studies purchase 11-61 62 antimatter 111 idle 151-214 222 223 225 231 233
start ec 11
wait ec11 completions >= 5
auto infinity 1e+100 x highest
wait ec11 completions >= 5
auto infinity 1e+1000 x highest
auto eternity 1e+100 x highest
studies purchase 11-61 62 time 111 active 151-214 72 82 92 102 dark
wait ep >=1e+1500
studies respec
eternity
while ep < 1e+10000 {
auto infinity off
auto eternity off
studies nowait purchase 11-111 time 111 active 151-214 dark
start dilation
pause 3s
studies respec
eternity
studies nowait purchase 11-111 time 111 active 151-214 dark
pause 10s
studies respec
eternity
}
