import unittest

from selenium import webdriver


class FrameDemo(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome()

        self.browser.get('https://skryabin.com/webdriver/html/sample.html')

    def tearDown(self) -> None:
        self.browser.quit()

    def test_frame_fields(self):
        browser = self.browser

        #        I. Outside a Frame

        #  First, we have to locate IFrame(frame) on the web page.
        #  There are 3 different mechanisms by which we can do this:
        #
        # – By using the tag name ( for example, ‘iframe’)
        #
        # – By using the Id of IFrame
        #
        # – By using the name of IFrame (in this case it is 'additionalInfo')

        # Second, we do the switching to IFrame using the following step:

        browser.switch_to.frame(browser.find_element_by_name('additionalInfo'))

        # Then, we can do some actions inside a frame

        #          II. Inside a Frame
        self.assertTrue(2 == len(browser.find_elements_by_tag_name('label')))

        displayed = browser.find_element_by_id('contactPersonName').is_displayed()
        self.assertTrue(displayed)
        browser.find_element_by_id("contactPersonName").send_keys("some text")
        # self.assertEqual("Contact Person Phone", browser.find_element_by_xpath("//*[@id='contactPersonPhone']/preceding::label[1]").text)

        #          III. Back to the parent HTML

        # You need to move back from an IFrame to the parent HTML.
        # Selenium Webdriver provides the following method:
        browser.switch_to.default_content()

        #          IV. Outside a Frame again
        displayed = browser.find_element_by_id('samplePageForm').is_displayed()
        self.assertTrue(displayed)


if __name__ == '__main__':
    unittest.main()
