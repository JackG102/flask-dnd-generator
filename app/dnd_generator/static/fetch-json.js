const fetchJson = endpoint => {
  fetch(endpoint)
  .then(request => {
    return request.json();
  })
  .then(data => {
    console.log(data);
    printJsonData(data);
  });
}

// TODO write functions that render the object specific to each item
// Pass them into this function as arguments 
const printJsonData = data => {
  const parsed_object = JSON.parse(JSON.stringify(data, undefined, 2));
  console.log(parsed_object);
  document.getElementById("target_json_container").innerHTML = "Converting JSON to HTML <br><br>" + 
  "Name: " + parsed_object.Name + 
  "<br>Race: " + parsed_object.Race +
  "<br>Gender: " + parsed_object.Gender +
  "<br>Vocation: " + parsed_object.Vocation +
  "<br>Alignment: " + parsed_object.Alignment;
}


