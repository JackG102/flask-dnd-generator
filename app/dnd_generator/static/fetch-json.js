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

const printJsonData = data => {
  document.getElementById("target_json_container").textContent = JSON.stringify(data, undefined, 2);
}


