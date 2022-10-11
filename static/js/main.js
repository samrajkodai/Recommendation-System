$(document).ready(function(){
    
    $("#input").on("input", function(){
        // Print entered value in a div box
        $("#result").text($(this).val());
       
        new_freq=$(this).val();
        $.ajax({ 
            url: '/predict', 
            type: 'POST', 
            data: {"new_freq":new_freq},
            success: function(response){ 
                console.log("success")
                console.log(typeof(response))
                setTimeout($('#result').text(' Result:  ' + response), 5000);
                var names = Object.values(response);
                word(names)
            } 
            })
    });
});


function word(sortedNames){

let input = document.getElementById("input");

input.addEventListener("keyup", (e) => {
removeElements();

for (let i of sortedNames) {
    console.log(i.substr(0, input.value.length));
  if (
    input.value != ""
  ) {
    //create li element
    let listItem = document.createElement("li");
    //One common class name
    listItem.classList.add("list-items");
    listItem.style.cursor = "pointer";
    listItem.setAttribute("onclick", "displayNames('" + i + "')");
    let word = "<b>" + i.substr(0, input.value.length) + "</b>";
    word += i.substr(input.value.length);
    //display the value in array
    listItem.innerHTML = word;
    document.querySelector(".list").appendChild(listItem);
  }
}
});
}


function displayNames(value) {
input.value = value;
removeElements();
}


function removeElements() {
//clear all the item
let items = document.querySelectorAll(".list-items");
items.forEach((item) => {
  item.remove();
});
}
