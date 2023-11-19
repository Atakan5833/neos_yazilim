async function user() {

    const container = document.querySelector(".container")
    //button
    const button = document.getElementById("button")
    //loader icon
    const loader = document.getElementById("loader")

    //butona tıklanınca loader gelsin
    loader.classList.remove("active")


    //fetch apı
    const request = await fetch("https://randomuser.me/api/?results=10");
    const response = await request.json()

    //api yüklenince loader gitsin
    loader.classList.add("active")

    button.disabled = true;
    button.title= "Daha fazlası için aşağı ininiz"

    //kullanıcıları foreach
    response.results.forEach(users => {
    console.log(users)
       const user = 
       `<div class="contents"> 
       <h3>${users.name.first+ " " + users.name.last}</h3>
        <div class="image">
       <img src='${users.picture.large}' alt="foto">
       <p><b>Phone: </b>${users.phone}</p>
        </div>
       </div>
       
       `
        container.innerHTML += user
    });














    

}

