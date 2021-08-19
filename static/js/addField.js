let count = 2
function appendFields(){
    document.querySelector('#save').addEventListener('click',(event)=>{
        try {
            event.preventDefault()
            if(count <=10){
                let name = document.getElementById('dirname').value
                console.log(name)
                let sidebar_list = document.getElementById('sidebar-list')

                //List item
                let listItem = document.createElement("li")
                listItem.id = 'listItem'+count

                //Append the list item
                sidebar_list.appendChild(listItem)

                //Parent div
                let div_container = document.createElement('div')
                div_container.classList.add('sidebar-inner-container')
                div_container.id = 'documentContainer'+count

                //Inner div
                let inner_div = document.createElement("div")
                inner_div.id='div'
                inner_div.innerHTML=name+' >'

                //Inner  List
                let inner_list = document.createElement("ul")
                inner_list.classList.add('sidebar-inner-list')
                inner_list.id = 'innerList'+count

                //Inner list item
                let inner_list_item = document.createElement("li")
                //Button
                let button = document.createElement("button")
                button.type="button"
                button.classList.add("btn-inner")
                button.value="+"
                button.innerHTML = "+"
                button.id = "documentButton"+count

                //Append the button to the inner list
                inner_list_item.appendChild(button)
                //Append the list item to the list
                inner_list.appendChild(inner_list_item)
                //Append the list to the div
                inner_div.appendChild(inner_list)
                //Append Inner div to the parent div
                div_container.appendChild(inner_div)

                //Append all to the list
                listItem.appendChild(div_container)
                
            }
            else{
                alert('You can not add more than 10 directories')
            }   
        } catch (error) {
            console.log('Error:',error)
        }
    })
}
function addDocument(){
    const buttons = document.querySelectorAll("button.btn-inner").forEach((element)=>{
        element.addEventListener('click',(event)=>{
            event.preventDefault()
            console.log('clicked')
        })
    })
    console.log(buttons)
}
appendFields()
addDocument()