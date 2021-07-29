<!--    select all .cards-item-wrapper items to make shadow upon hovering over image-->
// const cardsItems = document.querySelectorAll('.cards-item-wrapper')

const cardsItems = document.querySelectorAll('.card-review-wrapper')
cardsItems.forEach(cardsItem => {
    cardsItem.addEventListener('mouseover', () => {
        // cardsItem.classList.add('img-darken')
        // cardsItem.childNodes[0].classList.add('img-darken')
        cardsItem.children[0].classList.add('img-darken')
    })

    cardsItem.addEventListener('mouseout', () => {
        // cardsItem.classList.remove('img-darken')
        // cardsItem.childNodes[0].classList.remove('img-darken')
        cardsItem.children[0].classList.remove('img-darken')
    })

    })

//Modal 1
//https://github.com/WebDevSimplified/Vanilla-JavaScript-Modal
const openModalButtons = document.querySelectorAll('[data-modal-target]')
const closeModalButtons = document.querySelectorAll('[data-close-button]')
const overlay = document.getElementById('overlay')

openModalButtons.forEach(button => {
  button.addEventListener('click', () => {
    const modal = document.querySelector(button.dataset.modalTarget)
    openModal(modal)
  })
})

overlay.addEventListener('click', () => {
  const modals = document.querySelectorAll('.modal.active')
  modals.forEach(modal => {
    closeModal(modal)
  })
})

closeModalButtons.forEach(button => {
  button.addEventListener('click', () => {
    const modal = button.closest('.modal')
    closeModal(modal)
  })
})

function openModal(modal) {
  if (modal == null) return
  modal.classList.add('active')
  overlay.classList.add('active')
}

function closeModal(modal) {
  if (modal == null) return
  modal.classList.remove('active')
  overlay.classList.remove('active')
}