//火箭发射倒计时：
//for循环
function countdown(number){
  for(var i = number; i >= 0; i--) {
    console.log(i);
  }
}
//递归
function countdown(number){
  console.log(number);
  countdown(number -1);
}