def wishlist_item_count(request):

    count=0

    if request.user.is_authenticated:

        count=request.user.basket.basket_item.filter(is_order_placed=False).count()

    return {"cart_item_count":count}