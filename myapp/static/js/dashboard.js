

    
new Vue({
    el: '#app',
    delimiters: ['${','}'],
    data: function () {
      return {
        drawerState: true,
     
        employee_list : [],
        profile_list : [],
        token : '',
        global_hostname : '',
        no_account_employee : '',
        mark_as_read : [],
        dash : {
            backgroundColor : 'orange',
           color : 'white'
           },
           Deliberation : {
           backgroundColor : 'white',
           color : 'gray',
       },

       employee : {
            backgroundColor : 'white',
           color : 'gray'
           },
           performance_evaluation : {
           backgroundColor : 'white',
           color : 'gray',
       },
       settings : {
            backgroundColor : 'white',
           color : 'gray'
           },
           Deliberation : {
           backgroundColor : 'white',
           color : 'gray',
       },
        offline : [
            {
            id: 5,
            name: 'Brunhilde Panswick',
            email: 'bpanswick4@csmonitor.com',
            avatar: 'avatar2.jpg'
          },
           {
            id: 6,
            name: 'Winfield Stapforth',
            email: 'wstapforth5@pcworld.com',
            avatar: 'avatar6.jpg'
          }
        ],
        options_year :[
            
                '2015','2019',
            
        ],
        year : '',
        pic_user : 'http://res.heraldm.com/phpwas/restmb_jhidxmake.php?idx=5&simg=201701181539234376570_20170118154018_02.jpg',

       
      }
    },mounted () {
        
        



        this.employee_growth()
        this.employee_violation_growth()
        this.employee_deliberation_report()
        this.customer_concerns()

       
        

       



    },
    beforeMount () {
        var hostname = window.location.hostname;
        if(hostname == '127.0.0.1' || hostname == 'localhost'){

            hostname = hostname+':8000'
        }
        else{
            hostname = hostname
        }

       
	 this.global_hostname = `${window.location.protocol}//${hostname}`
     var csrftoken = Cookies.get('csrftoken');
     this.token = csrftoken
     this.get_employee()
      
     
        
        
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
        get_employee_mark_as_read(){

            var data = this.mark_as_read
            var emplist = this.employee_list

            var employee = []
           
            for (let index = 0; index < emplist.length; index++) {
                const element = emplist[index];
                    var emp = element.EmpCode
                    var obj = data.filter(
                        function(el){
                            return el.empcode == emp
                        }
                    )

                    employee.push(obj)

                    if(index == emplist.length - 1 ){
                            this.mark_as_read = employee
                            console.log(`final mark`)
                            console.log(this.mark_as_read)

                    }

                
            }


        },
        get_mark_as_read(){
            axios.get(`${this.global_hostname}/api/GET_PROFILE/`,{
                 headers: {
                             'Content-Type': 'application/json',
                                'X-CSRFToken': this.token
                 }
                
            })
            .then(res => {
                console.log(res)

                var data = res.data
                var filtered = data.filter(function(el){ return el.markasread == false})
                this.mark_as_read = filtered
                console.log('mark as read')
                console.log(this.mark_as_read)
                if(this.mark_as_read.length > 0){
                    this.get_employee_mark_as_read()
                }

            })
            .catch(err => {
                console.error(err); 
            })
        },


        send_post_to_create(empcode){

                var emp = empcode
                var emplist = this.employee_list
                var employee = emplist.filter(function(el){return  el.EmpCode == emp})


                let data = new FormData()
                data.append('empcode',emp)
                data.append('firstname',employee[0].FirstName)
                axios.post(`${this.global_hostname}/createaccount/`,data,{
                 
                     headers: {
                                 'Content-Type': 'application/json',
                                    'X-CSRFToken': this.token
                     }
                    
                })
                .then(res => {
                    console.log('created')
                    console.log(res)
                })
                .catch(err => {
                    console.error(err);
                    this.$q.notify({ //put dollor sign(q)
                              message: `Unsuccessfull - unstable connections!`,
                              timeout: 10000, // in milliseconds; 0 means no timeout

                              color: 'red',
                              textColor: 'white', // if default 'white' doesn't fit
                             icon: 'error', //or  avatar: 'statics/boy-avatar.png',

                             position: 'top', // 'top', 'left', 'bottom-left' etc.

                              }) 
                })
        },
        create_account_employee(){
            var data  = this.no_account_employee
            
            data.forEach(element => {
                this.send_post_to_create(element)    
            });
        },
        get_compare(){

            var profile = this.profile_list
            var emplist = this.employee_list
            var no_account = []
            for (let index = 0; index < emplist.length; index++) {
                const element =  emplist[index];    
               
                var info = profile.filter(function(el){return  el.empcode == element.EmpCode })
                if(info.length== 0){
                    no_account.push(element.EmpCode)
                }


                if(index == emplist.length - 1){
                    this.no_account_employee = no_account
                    console.log(this.no_account_employee)
                    this.create_account_employee()
                    this.get_mark_as_read()  
                }
               
                   
              
            }
            
            this.get_mark_as_read()
            


          

        },
        get_profile(){
            axios.get(`${this.global_hostname}/api/GET_PROFILE/`,{
                
                 headers: {
                             'Content-Type': 'application/json',
                                'X-CSRFToken': this.token
                 }
                
            })
            .then(res => {
                console.log(`profile`)
                this.profile_list = res.data
                console.log(this.profile_list)
                this.get_compare()
            })
            .catch(err => {
                console.error(err); 
            })
        },

        get_employee(){
            axios.get(`${this.global_hostname}/api/Employee/`,{
                
                 headers: {
                             'Content-Type': 'application/json',
                                'X-CSRFToken': this.token
                 }
                
            })
            .then(res => {
                console.log(`employee`)
                this.employee_list = res.data
                console.log(this.employee_list)
                this.get_profile()
            })
            .catch(err => {
                console.error(err); 
            })
        },
        employee_growth() {
            var ctx = document.getElementById('myChart').getContext('2d');
            var chart = new Chart(ctx, {
                // The type of chart we want to create
                type: 'line',

                // The data for our dataset
                data: {
                    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July','August','September','October','November','December'],
                    datasets: [{
                        label: 'Overall Growth of Employee Performance',
                        backgroundColor: 'rgb(244, 246, 246',
                        borderColor: 'rgb(231, 76, 60)',
                        data: [85, 75, 78, 78, 78, 78, 89,90, 85, 75, 96, 97],
                        fill : false
                    }]
                },

                // Configuration options go here
                options: {
                   
                }
            });
        },
        employee_violation_growth(){
            var ctx = document.getElementById('employee_violation').getContext('2d');
            var chart = new Chart(ctx, {
                // The type of chart we want to create
                type: 'line',
                

                // The data for our dataset
                data: {
                    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July','August','September','October','November','December'],
                    datasets: [{
                        label: 'Regularized',
                        backgroundColor: 'rgb(244, 246, 246',
                        borderColor: 'rgb(192, 57, 43)',
                        data: [85, 75, 78, 78, 78, 78, 89,90, 85, 75, 96, 97],
                        fill : false
                    },
                    {
                        label: 'Termination of Contract',
                        backgroundColor: 'rgb(244, 246, 246',
                        borderColor: 'rgb(82, 190, 128)',
                        data: [85, 5, 78, 85, 89, 78, 72,63, 45, 75, 82, 74],
                        fill : false

                    },
                    {
                        label: 'Termination of Contract with Chance',
                        backgroundColor: 'rgb(244, 246, 246',
                        borderColor: 'rgb(230, 126, 34)',
                        data: [25, 56, 89, 54, 41, 56, 54,26, 89, 45, 54, 32],
                        fill : false
                    }
                
                ],
                    
                },

                // Configuration options go here
                options: {}
            });
        },
        employee_deliberation_report(){
            var ctx = document.getElementById('employee_deliberation_growth').getContext('2d');
            var chart = new Chart(ctx, {
                // The type of chart we want to create
                type: 'line',

                // The data for our dataset
                data: {
                    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July','August','September','October','November','December'],
                    datasets: [{
                        label: 'Grave',
                        backgroundColor: 'rgb(244, 246, 246',
                        borderColor: 'rgb(192, 57, 43)',
                        data: [85, 75, 78, 78, 78, 78, 89,90, 85, 75, 96, 97],
                        fill : false
                    },
                    {
                        label: 'Minor',
                        backgroundColor: 'rgb(244, 246, 246',
                        borderColor: 'rgb(82, 190, 128)',
                        data: [85, 5, 78, 85, 89, 78, 72,63, 45, 75, 82, 74],
                        fill : false
                    }
                
                ],
                    
                },

                // Configuration options go here
                options: {}
            });
        },
        customer_concerns(){

            var ctx = document.getElementById('customer_concerns').getContext('2d');
            var chart = new Chart(ctx, {
                // The type of chart we want to create
                type: 'line',

                // The data for our dataset
                data: {
                    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July','August','September','October','November','December'],
                    datasets: [{
                        label: 'Complaints',
                        backgroundColor: 'rgb(244, 246, 246',
                        borderColor: 'rgb(192, 57, 43)',
                        data: [85, 75, 78, 78, 78, 78, 89,90, 85, 75, 96, 97],
                        fill : false
                    },
                    {
                        label: 'Complement',
                        backgroundColor: 'rgb(244, 246, 246',
                        borderColor: 'rgb(82, 190, 128)',
                        data: [85, 5, 78, 85, 89, 78, 72,63, 45, 75, 82, 74],
                        fill : false
                    },
                    {
                        label: 'Suggestions',
                        backgroundColor: 'rgb(244, 246, 246',
                        borderColor: 'rgb(246, 126, 20)',
                        data: [55, 18, 96, 45, 74, 75, 71,52, 74, 63, 52, 45],
                        fill : false
                    }
                
                ],
                    
                },

                // Configuration options go here
                options: {}
            });
        }
    },
})







