const navbar = document.getElementById("navbar");

window.addEventListener("scroll", () => {
    navbar.classList.toggle("scrolled", window.scrollY > 40);
});

function toggleMenu() {
    document.getElementById("navLinks").classList.toggle("active");
}

// Booking Modal

const modal = document.getElementById("modal");

function openModal() {
    modal.style.display = "flex";
}

function closeModal() {
    modal.style.display = "none";

    step1.classList.remove("hide");
    step2.classList.add("hide");
    step3.classList.add("hide");
}

function nextStep(step) {

    if(step===1){
        step1.classList.add("hide");
        step2.classList.remove("hide");
    }

    if(step===2){
        step2.classList.add("hide");
        step3.classList.remove("hide");
    }

}

// Animated Counters

function animateCounter(id,target,suffix=""){

    let value=0;

    const el=document.getElementById(id);

    const interval=setInterval(()=>{

        value+=Math.ceil(target/40);

        if(value>=target){

            value=target;

            clearInterval(interval);

        }

        el.textContent=value+suffix;

    },30);

}

const observer=new IntersectionObserver(entries=>{

    if(entries[0].isIntersecting){

        animateCounter("s1",500,"+");
        animateCounter("s2",1000,"+");

        document.getElementById("s3").textContent="4.8★";

        observer.disconnect();

    }

});

observer.observe(document.querySelector(".stats"));