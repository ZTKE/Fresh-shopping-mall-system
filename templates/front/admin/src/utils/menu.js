const menu = {
    list() {
        return [{"backMenu":[{"child":[{"appFrontIcon":"cuIcon-copy","buttons":["新增","查看","修改","删除"],"menu":"user","menuJump":"列表","tableName":"yonghu"}],"menu":"user management"},{"child":[{"appFrontIcon":"cuIcon-full","buttons":["新增","查看","修改","删除","查看评论"],"menu":"Commodity information","menuJump":"列表","tableName":"shangpinxinxi"}],"menu":"Commodity information management"},{"child":[{"appFrontIcon":"cuIcon-wenzi","buttons":["新增","查看","修改","删除"],"menu":"Commodity type","menuJump":"列表","tableName":"shangpinleixing"}],"menu":"Commodity type management"},{"child":[{"appFrontIcon":"cuIcon-news","buttons":["新增","查看","修改","删除"],"menu":"Announcement information","tableName":"news"},{"appFrontIcon":"cuIcon-goodsnew","buttons":["查看","修改"],"menu":"Rotation map management","tableName":"config"}],"menu":"system management"},{"child":[{"appFrontIcon":"cuIcon-copy","buttons":["查看","发货"],"menu":"Paid orders","tableName":"orders/已支付"},{"appFrontIcon":"cuIcon-send","buttons":["查看"],"menu":"Refunded order","tableName":"orders/已退款"},{"appFrontIcon":"cuIcon-explore","buttons":["查看"],"menu":"Completed order","tableName":"orders/已完成"},{"appFrontIcon":"cuIcon-album","buttons":["查看"],"menu":"Shipped order","tableName":"orders/已发货"},{"appFrontIcon":"cuIcon-discover","buttons":["查看"],"menu":"Unpaid orders","tableName":"orders/未支付"},{"appFrontIcon":"cuIcon-rank","buttons":["查看"],"menu":"Order cancelled","tableName":"orders/已取消"}],"menu":"Order management"}],"frontMenu":[{"child":[{"appFrontIcon":"cuIcon-circle","buttons":["查看","查看评论"],"menu":"Commodity information列表","menuJump":"列表","tableName":"shangpinxinxi"}],"menu":"Commodity information模块"}],"hasBackLogin":"是","hasBackRegister":"否","hasFrontLogin":"否","hasFrontRegister":"否","roleName":"管理员","tableName":"users"},{"backMenu":[{"child":[{"appFrontIcon":"cuIcon-favor","buttons":["查看","删除"],"menu":"我的收藏管理","tableName":"storeup"}],"menu":"我的收藏管理"},{"child":[{"appFrontIcon":"cuIcon-album","buttons":["查看"],"menu":"Shipped order","tableName":"orders/已发货"},{"appFrontIcon":"cuIcon-discover","buttons":["查看"],"menu":"Unpaid orders","tableName":"orders/未支付"},{"appFrontIcon":"cuIcon-rank","buttons":["查看"],"menu":"Order cancelled","tableName":"orders/已取消"},{"appFrontIcon":"cuIcon-copy","buttons":["查看"],"menu":"Paid orders","tableName":"orders/已支付"},{"appFrontIcon":"cuIcon-send","buttons":["查看"],"menu":"Refunded order","tableName":"orders/已退款"},{"appFrontIcon":"cuIcon-explore","buttons":["查看"],"menu":"Completed order","tableName":"orders/已完成"}],"menu":"Order management"}],"frontMenu":[{"child":[{"appFrontIcon":"cuIcon-circle","buttons":["查看","查看评论"],"menu":"Commodity information列表","menuJump":"列表","tableName":"shangpinxinxi"}],"menu":"Commodity information模块"}],"hasBackLogin":"是","hasBackRegister":"否","hasFrontLogin":"是","hasFrontRegister":"是","roleName":"user","tableName":"yonghu"}]
    }
}
export default menu;