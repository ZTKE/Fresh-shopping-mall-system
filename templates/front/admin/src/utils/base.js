const base = {
    get() {
        return {
            url : "http://localhost:8080/django4j60g/",
            name: "django4j60g",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "fresh market system"
        } 
    }
}
export default base
