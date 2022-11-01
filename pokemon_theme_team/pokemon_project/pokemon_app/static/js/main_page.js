
async function buttonClick(){
pokemon=document.getElementById("pokemon_name").value
console.log(pokemon)
axios.get(`/get_pokemon/${pokemon}`)
.then((response)=>{
console.log(response)
for (x of Object.keys(response.data)){
console.log(response.data[`${x}`])
document.getElementById(`${x}`).src=response.data[`${x}`]
}
}
)

}