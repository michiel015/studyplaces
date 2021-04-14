<!--    select all .cards-item-wrapper items to make shadow upon hovering over image-->
// const cardsItems = document.querySelectorAll('.cards-item-wrapper')

// const cardsItems = document.querySelectorAll('.cards-img-background')
// cardsItems.forEach(cardsItem => {
//     cardsItem.addEventListener('mouseover', () => {
//         cardsItem.classList.add('img-darken')
//         // cardsItem.childNodes[1].classList.add('img-darken')
//         // cardsItem.children[1].classList.add('img-darken')
//     })
//
//     cardsItem.addEventListener('mouseout', () => {
//         cardsItem.classList.remove('img-darken')
//         // cardsItem.childNodes[1].classList.remove('img-darken')
//         // cardsItem.children[1].classList.add('img-darken')
//     })
//
//     })

// Get the button that opens the modal
var btn = document.querySelectorAll("button.modal-button");

// All page modals
var modals = document.querySelectorAll('.modal');

// Get the <span> element that closes the modal
var spans = document.getElementsByClassName("close");

// When the user clicks the button, open the modal
for (var i = 0; i < btn.length; i++) {
 btn[i].onclick = function(e) {
    e.preventDefault();
    modal = document.querySelector(e.target.getAttribute("href"));
    modal.style.display = "block";
 }
}

// When the user clicks on <span> (x), close the modal
for (var i = 0; i < spans.length; i++) {
 spans[i].onclick = function() {
    for (var index in modals) {
      if (typeof modals[index].style !== 'undefined') modals[index].style.display = "none";
    }
 }
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target.classList.contains('modal')) {
     for (var index in modals) {
      if (typeof modals[index].style !== 'undefined') modals[index].style.display = "none";
     }
    }
}