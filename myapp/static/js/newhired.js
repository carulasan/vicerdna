
new Vue({
    el: '#app',
    delimiters: ['${','}'],
    data: function () {
      return {

   
        employee_list : [],
        profile_list : [],
        token : '',
        global_hostname : '',
        no_account_employee : '',
        mark_as_read : [],
      }
    },mounted () {
        
        



        

       



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
   
    },
})


