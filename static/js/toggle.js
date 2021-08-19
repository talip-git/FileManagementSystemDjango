function toggleInnerList (){
    try {
        $(document).click((event)=>{
            if(event.target.children.length==1 && event.target !=undefined){
                if(event.target.children[0].id !=undefined){
                    let target = event.target.children[0].id   
                    if(target){
                        $('#'+target).fadeToggle()
                    }
                }
            }
        })        
    } catch (error) {
        console.log(error)
    }
}
toggleInnerList()