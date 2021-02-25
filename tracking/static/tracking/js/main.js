
function obtenerHuella(){
	Fingerprint2.getV18(function (result, components) {
      $( "#fp" ).val(result)
      $( "#fp2" ).val(result)
      $( "#components" ).val(JSON.stringify(components))
      $( "#results" ).empty().append('<tr><th>Su identificador único (hash) es:</th><td>' + result + '</td></tr>');
      var info;
      components.forEach((item, i) => {
        info = '<tr><th>' + item.key + ': </th><td>' + item.value + '</td></tr>';
        if (item.key == 'canvas'){
          info = '<tr><th>' + item.key + ': </th><td>' + "<img id = 'canvasfp' src =" + String(item.value).split("canvas fp:")[1] + "></td></tr>";
        }
        if (item.key == 'webgl'){
          info = '<tr><th>' + item.key + ': </th><td>' +"<img id = 'webGL' src =" + String(item.value).split('~')[0] + "></td></tr>";
          /*info = '<li><span>' + item.key + ': ' + item.value.split('~')[0] + '</span></li>';*/
        }
        $( "#results" ).append(info);
      });
		});
  return false;
}


$(document).ready(function(){
    obtenerHuella()
});
