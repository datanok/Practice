
interface Iuser {
    id: number,
    name: string,
    email: string
}
interface IUserManger {
    users: Iuser []
    nextId: number
}


class UserManager implements IUserManger{
    users: Iuser [];
    nextId: number;
    constructor(name : string,email : string){
        this.users = []
        this.nextId = 1;

        if(name && email){
            this.addUser(name,email)
        }

    }
    addUser(name: string, email:string ):Iuser {
        const newUser : Iuser = {id:this.nextId++, name, email}
        this.users.push(newUser)
        return newUser
    }

    listUsers():Iuser []{
        return this.users
    }
    
    getUser(id:number){
        return this.users.find((u => u.id === id))
    }

    deleteUser(id:number): Iuser | null {
        const userIdx = this.users.findIndex((u)=> u.id===id)
        if (userIdx === -1)return null
        const [deletedUser] = this.users.splice(userIdx,1)
        return deletedUser
    }
    
    deleteAll(): number{
        const deletedUsers: Iuser[] = this.users
        this.users = []
        return deletedUsers.length
    }
    updateUser(id:number,updatedUserData:Iuser){
        const user = this.getUser(id)
        if (!user) return null
        user.email = updatedUserData.email
        user.name = updatedUserData.name
        return user
    }
}

module.exports = UserManager; 