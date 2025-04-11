if ep < 1e+1 {
  auto infinity 1e+10 x highest
  auto eternity 1e+1 x highest
  studies purchase 11-61 time 111
  wait ep >=1e+1
}
if ep < 1e+10 {
  auto infinity 1e+100 x highest
  auto eternity 1e+1 x highest
  studies purchase 11-61, 62, time, 111, idle, 151-171
  wait ep >=1e+10
}
if ec2 completions < 1 {
  studies purchase 11-61, 62, time, 111, idle, 151-171
  start ec 2
  wait pending ip >= 1e+975
  infinity
}
if ec2 completions < 2 {
  studies purchase 11-61, 62, time, 111, idle, 151-171
  start ec 2
  wait pending ip >= 1e+1150
  infinity
}
if ec3 completions < 1 {
  studies purchase 11-61, 62, antimatter, 111, idle, 151-171
  start ec 3
  wait pending ip >= 1e+600
  infinity
}
if ep < 1e+28 {
  auto infinity 1e+100 x highest
  auto eternity 1e+1 x highest
  studies purchase 11-61, 62, time, 111, idle, 151-171
  wait ep >=1e+28
}
if eternities < 1e+5 {
  auto infinity 1.8e+308 ip
  auto eternity 1 ep
  wait eternities > 1e+5
  auto infinity 1e+100 x highest
  auto eternity 1e+10 x highest
}
if ec1 completions < 1 {
  studies purchase 11-61, 62, antimatter, 111, idle, 151-171
  start ec 1
  wait pending ip >= 1e+1800
  infinity
}
if ec1 completions < 2 {
  studies purchase 11-61, 62, antimatter, 111, idle, 151-171
  start ec 1
  wait pending ip >= 1e+2000
  infinity
}
if ec2 completions < 3 {
  studies purchase 11-61, 62, antimatter, 111, idle, 151-171
  start ec 2
  wait pending ip >= 1e+1325
  infinity
}
if ec1 completions < 3 {
  studies purchase 11-61, 62, infinity, 111, idle, 151-171
  start ec 1
  wait pending ip >= 1e+2200
  infinity
}
if ep < 1e+33 {
  auto infinity 1e+250 x highest
  auto eternity 1e+1 x highest
  studies purchase 11-61, 62, time, 111, idle, 151-171
  wait ep >=1e+33
}
if ec3 completions < 2 {
  studies purchase 11-61, 62, antimatter, 111, idle, 151-171
  start ec 3
  wait pending ip >= 1e+675
  infinity
}
if ec1 completions < 4 {
  studies purchase 11-61, 62, infinity, 111, idle, 151-171
  start ec 1
  wait pending ip >= 1e+2400
  infinity
}
if ec1 completions < 5 {
  studies purchase 11-61, 62, infinity, 111, idle, 151-171
  start ec 1
  wait pending ip >= 1e+2600
  infinity
}
if ec3 completions < 3 {
  studies purchase 11-61, 62, antimatter, 111, idle, 151-171
  start ec 3
  wait pending ip >= 1e+750
  infinity
}
if ec3 completions < 5 {
  auto infinity 1e+1 x highest
  studies purchase 11-61, 62, time, 111, idle, 151-171
  start ec 3
  wait pending ip >= 1e+900
  infinity
}
if ec2 completions < 4 {
  studies purchase 11-61, 62, antimatter, 111, idle, 151-171
  start ec 2
  wait pending ip >= 1e+1500
  infinity
}
if ec2 completions < 5 {
  studies purchase 11-61, 62, time, 111, idle, 151-171
  start ec 2
  wait pending ip >= 1e+1675
  infinity
}
if ec3 completions < 4 {
  studies purchase 11-61, 62, antimatter, 111, idle, 151-171
  start ec 3
  wait pending ip >= 1e+825
  infinity
}
if ec4 completions < 1 {
  auto infinity 5.1s
  studies purchase 11-61, 62, time, 111, idle, 151-171
  start ec 4
  wait pending ip >= 1e+2750
  infinity
  auto infinity 1e+100 x highest
}
if ec4 completions < 2 {
  auto infinity 5.1s
  studies purchase 11-61, 62, time, 111, idle, 151-171
  start ec 4
  wait pending ip >= 1e+3300
  infinity
  auto infinity 1e+100 x highest
}
if ec4 completions < 3 {
  auto infinity 5.1s
  studies purchase 11-61, 62, time, 111, idle, 151-171
  start ec 4
  wait pending ip >= 1e+3850
  infinity
  auto infinity 1e+100 x highest
}
if ep < 1e+40 {
  auto infinity 1e+100 x highest
  auto eternity 1e+1 x highest
  studies purchase 11-61, 62, time, 111, idle, 151-171
  wait ep >=1e+40
}
if ec5 completions < 1 {
  studies purchase 11-61, 62, time, 111, idle, 151-171
  start ec 5
  wait pending ip >= 1e+750
  infinity
}
if ec5 completions < 2 {
  studies purchase 11-61, 62, time, 111, idle, 151-171
  start ec 5
  wait pending ip >= 1e+1150
  infinity
}
if ec5 completions < 3 {
  studies purchase 11-61, 62, time, 111, idle, 151-171
  start ec 5
  wait pending ip >= 1e+1550
  infinity
}
if ec5 completions < 4 {
  studies purchase 11-61, 62, time, 111, idle, 151-171
  start ec 5
  wait pending ip >= 1e+1950
  infinity
}
if ec5 completions < 5 {
  studies purchase 11-61, 62, time, 111, idle, 151-171
  start ec 5
  wait pending ip >= 1e+2350
  infinity
}
if ec4 completions < 4 {
  auto infinity 5.1s
  studies purchase 11-61, 62, time, 111, idle, 151-171
  start ec 4
  wait pending ip >= 1e+4400
  infinity
  auto infinity 1e+100 x highest
}
if ep < 1e+50 {
  auto infinity 1e+200 x highest
  auto eternity 1e+1 x highest
  studies purchase 11-61, 62, time, 111, idle, 151-171
  wait ep >=1e+50
}
if ec6 completions < 1 {
  auto infinity off
  studies purchase 11-61, 62, time, 111, active, 151-171, 181
  start ec 6
  wait pending ip >= 1e+850
  infinity
  auto infinity 1e+100 x highest
}
if ec6 completions < 2 {
  auto infinity off
  studies purchase 11-61, 62, time, 111, active, 151-171, 181
  start ec 6
  wait pending ip >= 1e+1100
  infinity
  auto infinity 1e+100 x highest
}
if ec6 completions < 3 {
  auto infinity off
  studies purchase 11-61, 62, time, 111, active, 151-171, 181
  start ec 6
  wait pending ip >= 1e+1350
  infinity
  auto infinity 1e+100 x highest
}
if ec6 completions < 4 {
  auto infinity off
  studies purchase 11-61, 62, time, 111, active, 151-171, 181
  start ec 6
  wait pending ip >= 1e+1600
  infinity
  auto infinity 1e+100 x highest
}
if ec6 completions < 5 {
  auto infinity off
  studies purchase 11-61, 62, time, 111, active, 151-171, 181
  start ec 6
  wait pending ip >= 1e+1850
  infinity
  auto infinity 1e+100 x highest
}
if ec7 completions < 1 {
  studies purchase 11-61, 62, time, 111, idle, 151-171
  start ec 7
  wait pending ip >= 1e+2000
  infinity
}
if ec7 completions < 2 {
  studies purchase 11-61, 62, time, 111, idle, 151-171
  start ec 7
  wait pending ip >= 1e+2530
  infinity
}
if ec7 completions < 3 {
  studies purchase 11-61, 62, time, 111, idle, 151-171
  start ec 7
  wait pending ip >= 1e+3060
  infinity
}
if ec7 completions < 4 {
  studies purchase 11-61, 62, time, 111, idle, 151-171
  start ec 7
  wait pending ip >= 1e+3590
  infinity
}
if ec8 completions < 1 {
  studies purchase 11-61, 62, time, 111, idle, 151-171
  start ec 8
  wait pending ip >= 1e+1300
  infinity
}
if ec8 completions < 2 {
  studies purchase 11-61, 62, time, 111, idle, 151-171
  start ec 8
  wait pending ip >= 1e+2200
  infinity
}
if ec8 completions < 3 {
  studies purchase 11-61, 62, time, 111, idle, 151-171
  start ec 8
  wait pending ip >= 1e+3100
  infinity
}
if ec9 completions < 1 {
  auto infinity off
  studies purchase 11-61, 62, time, 111, active, 151-171, 181
  start ec 9
  wait pending ip >= 1e+1750
  infinity
  auto infinity 1e+100 x highest
}
if ec9 completions < 2 {
  auto infinity off
  studies purchase 11-61, 62, time, 111, active, 151-171, 181
  start ec 9
  wait pending ip >= 1e+2000
  infinity
  auto infinity 1e+100 x highest
}
if ec9 completions < 3 {
  auto infinity off
  studies purchase 11-61, 62, time, 111, active, 151-171, 181
  start ec 9
  wait pending ip >= 1e+2250
  infinity
  auto infinity 1e+100 x highest
}
if ec9 completions < 4 {
  auto infinity off
  studies purchase 11-61, 62, time, 111, active, 151-171, 181
  start ec 9
  wait pending ip >= 1e+2500
  infinity
  auto infinity 1e+100 x highest
}
if ec9 completions < 5 {
  auto infinity off
  studies purchase 11-61, 62, time, 111, active, 151-171, 181
  start ec 9
  wait pending ip >= 1e+2750
  infinity
  auto infinity 1e+100 x highest
}
