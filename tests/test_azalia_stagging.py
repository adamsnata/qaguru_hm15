import allure
from selene import have, browser, be
from selene.support.shared import browser


@allure.title("Проверка что избранное пустое изначально")
def test_check_empty_favorites():
    browser.open('')
    browser.element('[data-testid="banner-mobile-app-close"]').click()  # close advertisment
    browser.all('[data-testid="favorites"]').filtered_by(be.visible).first.click()
    #browser.all('[data-testid="favorites"]')[1].click()
    browser.element('[class^="Favorites_empty__title__"]').should(have.exact_text('Здесь пока пусто'))


@allure.title("Проверка что есть 2 города на главной странице")
def test_check_2_cities():
    browser.open('')
    browser.element('[data-testid="banner-mobile-app-close"]').click()  # close advertisment
    browser.all('[data-testid="geo-toggler"]').filtered_by(be.visible).first.click()  # click listbox cities
    browser.all('[data-testid="geo-item"]')[0].should(have.text('Москва и Московская область'))
    browser.all('[data-testid="geo-item"]')[1].should(have.text('Нижний Новгород и Нижегородская область'))


@allure.title("Проверка что корзина изначально пустая")
def test_check_bin():
    browser.open('')
    browser.element('[data-testid="banner-mobile-app-close"]').click()  # close advertisment
    browser.all('[data-testid="checkout"]')[1].click()  # click bin
    browser.element('[class^="Favorites_empty__title__"]').should(have.text('В корзине пусто'))


@allure.title("Проверка что пользователь изначально не авторизован")
def test_check_user_not_authorised():
    browser.open('')
    browser.element('[data-testid="banner-mobile-app-close"]').click()  # close advertisment
    browser.all('[data-testid="open-login-modal"]')[1].should(have.text('Войти'))


@allure.title("Проверка что поиск работает и ищет")
def test_check_search_rozi():
    browser.open('')
    browser.element('[data-testid="banner-mobile-app-close"]').click()  # close advertisment
    browser.element('[inputmode="search"]').type("Розы").press_enter()
    browser.element('[class^="SearchCatalog_title__').should(have.text('розы'))
    browser.all('[class^="ProductCard_name__"]')[1].should(have.text("роз"))


@allure.title("Добавление любого товара в корзину и проверка что он добавлен")
def test_add_to_bin():
    browser.open('')
    browser.element('[data-testid="banner-mobile-app-close"]').click()  # close advertisment
    browser.all('[class^="ProductCard_cartButton__"]')[0].click()
    browser.all('[class ^="ProductsListItem_wrapper__"]')[0].should(have.text('1'))
