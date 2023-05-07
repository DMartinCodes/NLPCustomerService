// Get the value of the input form
const question = document.getElementById('question').value;

// Send a POST request to the server with the question data
fetch('/newmessage/' + question, {
  method: 'GET'
})
.then(response => {
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  // Do something with the response
    return response.json();

})
.catch(error => {
  console.error('There was a problem with the fetch operation:', error);
  
});

TweenMax.from(".logo", 1, {
  opacity: 0,
  x: -20,
  ease: Expo.easeInOut
})

TweenMax.staggerFrom("nav ul li", 1, {
  opacity: 0,
  x: -20,
  ease: Power3.easeInOut
}, 0.08)

TweenMax.from(".search", 1, {
  opacity: 0,
  delay: .5,
  x: -20,
  ease: Expo.easeInOut
})

TweenMax.from(".menu", 1, {
  opacity: 0,
  delay: .6,
  x: -20,
  ease: Expo.easeInOut
})

TweenMax.from(".title", 1, {
  opacity: 0,
  delay: 1,
  y: 20,
  ease: Expo.easeInOut
})

TweenMax.from(".btn", 1, {
  opacity: 0,
  delay: 1.6,
  y: 20,
  ease: Expo.easeInOut
})

TweenMax.from(".line-one", 1, {
  opacity: 0,
  delay: 2,
  y: -800,
  ease: Expo.easeInOut
})
TweenMax.from(".line-two", 1, {
  opacity: 0,
  delay: 2.5,
  y: -800,
  ease: Expo.easeInOut
})
TweenMax.from(".line-three", 1, {
  opacity: 0,
  delay: 3,
  y: -800,
  ease: Expo.easeInOut
})


TweenMax.from(".img", 2, {
  opacity: 0,
  delay: 2.9,
  y: -800,
  ease: Expo.easeInOut
})

TweenMax.from(".year", 1, {
  opacity: 0,
  delay: 1.4,
  y: -20,
  ease: Expo.easeInOut
})

TweenMax.staggerFrom(".media ul li", 2, {
  opacity: 0,
  delay: 3.2,
  y: 40,
  ease: Expo.easeInOut
}, 0.2)




