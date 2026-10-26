// reveal on scroll
const io=new IntersectionObserver((es)=>{es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('vis');io.unobserve(e.target)}})},{threshold:.12});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
// header solid + pagetop
const hd=document.getElementById('hd'),pt=document.querySelector('.pagetop');
function onScroll(){const y=window.scrollY;if(hd){hd.classList.toggle('solid',y>60||!document.querySelector('.hero'))}if(pt){pt.classList.toggle('show',y>500)}}
// pages without hero: header always solid
if(!document.querySelector('.hero')&&hd){hd.classList.add('solid')}
window.addEventListener('scroll',onScroll,{passive:true});onScroll();
// close mobile menu on link tap
document.querySelectorAll('.mnav a').forEach(a=>a.addEventListener('click',()=>document.body.classList.remove('mopen')));
