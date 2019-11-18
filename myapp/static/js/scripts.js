
new Vue({
    el: '#app',
    delimiters: ['${','}'],
    data: function () {
      return {
        drawerState: true,
        pic_user : 'http://res.heraldm.com/phpwas/restmb_jhidxmake.php?idx=5&simg=201701181539234376570_20170118154018_02.jpg',
        left : false,
        dash : {
  backgroundColor : 'white',
   color : 'gray',
   },
   Deliberation : {
   backgroundColor : 'white',
   color : 'gray',
},

employee : {
backgroundColor : 'white',
   color : 'gray',


   },
performance_evaluation : {
  backgroundColor : 'white',
   color : 'gray'

},
settings : {
backgroundColor : 'orange',
   color : 'white'
   },
Deliberation : {
   backgroundColor : 'white',
   color : 'gray',
},
global_hostname : '',
token : '',





       
      }
    },beforeMount () {
      if(innerWidth < 1017){
            this.drawerState = false
        }
    },
  methods: {
    logout(){
      axios.post(`${this.global_hostname}/logout/`,{
          
           headers: {
                       'Content-Type': 'application/json',
                          'X-CSRFToken': this.token
           }
          
      })
      .then(res => {
          window.location.replace(`${this.global_hostname}/login/`)
        
      })
      .catch(err => {
          
      })

      
},


  },
  mounted () {
    
    var hostname = window.location.hostname;
if(hostname == '127.0.0.1' || hostname == 'localhost'){

    hostname = hostname+':8000'
}
else{
    hostname = hostname
}

this.global_hostname = `${window.location.protocol}//${hostname}`;
var csrftoken = Cookies.get('csrftoken');
this.token = csrftoken




  },
})

