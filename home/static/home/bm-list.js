$(document).ready(function() {
     
    // For Search the items from bookmark
    const serchBar = document.forms["search"].querySelector('input');
    serchBar.addEventListener("keyup", function (e) {
        
        const term = e.target.value.toLowerCase();
        const items = list.getElementsByTagName("li");
        Array.from(items).forEach(function (item) {

            const title = item.firstElementChild.textContent;
            if (title.toLowerCase().indexOf(term) != -1) {
                item.style.display = "block";
            }
            else {
                item.style.display = "none";
            }
        });
    });
});