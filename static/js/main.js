<!--    select all .cards-item-wrapper items to make shadow upon hovering over image-->
// const cardsItems = document.querySelectorAll('.cards-item-wrapper')
const cardsItems = document.querySelectorAll('.cards-img-background')
cardsItems.forEach(cardsItem => {
    cardsItem.addEventListener('mouseover', () => {
        cardsItem.childNodes[1].classList.add('img-darken')
    })

    cardsItem.addEventListener('mouseout', () => {
        cardsItem.childNodes[1].classList.remove('img-darken')
    })

    })