const addQuantityBtn = document.querySelector("#add-quantity")
const quantityValue = document.querySelector("#quantity-value")
const minusQuantityBtn = document.querySelector("#minus-quantity")

addQuantityBtn.addEventListener("click",() => {
    if(isNaN(Number(quantityValue.value))===true || Number(quantityValue.value) < 1){
        quantityValue.value = 1 
        return
    }
    quantityValue.value = Number(quantityValue.value)+1 
})


minusQuantityBtn.addEventListener("click",() => {
    if(isNaN(Number(quantityValue.value))===true || Number(quantityValue.value) < 1){
        quantityValue.value = 1 
        return
    }
     if(Number(quantityValue.value)===1){
        quantityValue.value =1
        return 
    }
    quantityValue.value = Number(quantityValue.value)-1 
})



quantityValue.addEventListener("change",() => {
    if(isNaN(Number(quantityValue.value))===true || Number(quantityValue.value) < 1){
        quantityValue.value = 1
        return
    }

})