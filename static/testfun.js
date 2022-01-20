function testfun(){

const appUrl = 'https://prod-05.northcentralus.logic.azure.com:443/workflows/897e0dba354d42c98a016e9ec56b5b7e/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=nOxZnDGzdiP6DDcp6nVGkrrXt6rtb_eaQiAVpyJHH5Q';
const date = new Date(Date.now());
const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
let x = axios.post(appUrl, {
    id: `${self.crypto.getRandomValues(new Uint32Array(1))[0]}`,
    month: months[date.getMonth()],
    day: date.getDate(),
    year: date.getFullYear(),
    hour: date.getHours(),
    minute: date.getMinutes(),
    second: date.getSeconds()
  })
  .then(function (response) {
    console.log(response);
    return response.data
  });}
