"""<article>
<front>
    <article-meta>
      <pub-date publication-format="electronic" date-type="collection">
        <year>2003</year>
      </pub-date>
      <volume>4</volume>
      <issue>1</issue>
      <fpage>108</fpage>
      <lpage>123</lpage>
    </article-meta>
  </front>
</article>
"""
import sys
sys.path.append("/home/travis/builds/repos/scieloorg---packtools/")
from packtools.sps.models.dates import ArticleDates
from packtools.sps.models.article_ids import ArticleIds


<insert generated code here>


class ArticleMetaIssue:

    def __init__(self, xmltree):
        self.xmltree = xmltree

    @property
    def data(self):
        attr_names = (
            "volume", "number", "suppl",
            "fpage", "fpage_seq", "lpage",
            "elocation_id",
        )
        _data = {}
        for k in attr_names:
            try:
                value = getattr(self, k)
            except AttributeError:
                continue
            else:
                if value:
                    _data[k] = value
        try:
            _data["pub_year"] = self.collection_date["year"]
        except (KeyError, TypeError):
            pass
        return _data

    @property
    def collection_date(self):
        _date = ArticleDates(self.xmltree)
        return _date.collection_date

    @property
    def volume(self):
        return self.xmltree.findtext(".//front/article-meta/volume")

    @property
    def issue(self):
        return self.xmltree.findtext(".//front/article-meta/issue")

    @property
    def number(self):
        _issue = self.issue
        if _issue:
            n, s = _extract_number_and_supplment_from_issue_element(_issue)
            return n

    @property
    def suppl(self):
        _suppl = self.xmltree.findtext(".//front/article-meta/supplement")
        if _suppl:
            return _suppl
        _issue = self.issue
        if _issue:
            n, s = _extract_number_and_supplment_from_issue_element(_issue)
            return s

    @property
    def elocation_id(self):
        return self.xmltree.findtext(".//front/article-meta/elocation-id")

    @property
    def fpage(self):
        return self.xmltree.findtext(".//front/article-meta/fpage")

    @property
    def fpage_seq(self):
        try:
            return self.xmltree.xpath(".//front/article-meta/fpage")[0].get("seq")
        except IndexError:
            return None

    @property
    def lpage(self):
        return self.xmltree.findtext(".//front/article-meta/lpage")

    @property
    def order(self):
        _order = self.xmltree.findtext('.//article-id[@pub-id-type="other"]')
        if _order is None:
            _order = ArticleIds(self.xmltree).v2
        return int(_order)

if __name__ == "__main__":
    isT=True
    test_cases = dict()
    def t1():
        expected = "5", "0"
        try:
            result = _extract_number_and_supplment_from_issue_element("5 (suppl)")
            test_cases['test1'] = result
        except Exception as error :
            result = ''
            test_cases['test1'] = type(error).__name__
        return expected==result


    def t2():
        expected = "5", "0"
        try:
            result = _extract_number_and_supplment_from_issue_element("5 Suppl")
            test_cases['test2'] = result
        except Exception as error:
            result = ''
            test_cases['test2'] = type(error).__name__
        return expected== result


    def t3():
        expected = "5", "1"
        try:
            result = _extract_number_and_supplment_from_issue_element("5 Suppl 1")
            test_cases['test3'] = result
        except Exception as error:
            result = ''
            test_cases['test3'] = type(error).__name__
        return expected== result


    def t4():
        expected = "5spe", None
        try:
            result = _extract_number_and_supplment_from_issue_element("5 spe")
            test_cases['test4'] = result
        except Exception as error:
            result = ''
            test_cases['test4'] = type(error).__name__
        return expected== result


    def t5():
        expected = "5", "0"
        try:
            result = _extract_number_and_supplment_from_issue_element("5 suppl")
            test_cases['test5'] = result
        except Exception as error:
            result = ''
            test_cases['test5'] = type(error).__name__
        return expected== result


    def t6():
        expected = "5", "1"
        try:
            result = _extract_number_and_supplment_from_issue_element("5 suppl 1")
            test_cases['test6'] = result
        except Exception as error:
            result = ''
            test_cases['test6'] = type(error).__name__
        return expected== result


    def t7():
        expected = "5", "1"
        try:
            result = _extract_number_and_supplment_from_issue_element("5 suppl. 1")
            test_cases['test7'] = result
        except Exception as error:
            result = ''
            test_cases['test7'] = type(error).__name__
        return expected== result


    def t8():
        expected = "25", "1"
        try:
            result = _extract_number_and_supplment_from_issue_element("25 Suppl 1")
            test_cases['test8'] = result
        except Exception as error:
            result = ''
            test_cases['test8'] = type(error).__name__
        return expected== result


    def t9():
        expected = "2-5", "1"
        try:
            result = _extract_number_and_supplment_from_issue_element("2-5 suppl 1")
            test_cases['test9'] = result
        except Exception as error:
            result = ''
            test_cases['test9'] = type(error).__name__
        return expected== result


    def t10():
        expected = "2spe", None
        try:
            result = _extract_number_and_supplment_from_issue_element("2spe")
            test_cases['test10'] = result
        except Exception as error:
            result = ''
            test_cases['test10'] = type(error).__name__
        return expected== result


    def t11():
        expected = "spe", None
        try:
            result = _extract_number_and_supplment_from_issue_element("Spe")
            test_cases['test11'] = result
        except Exception as error:
            result = ''
            test_cases['test11'] = type(error).__name__
        return expected== result


    def t12():
        expected = None, "1"
        try:
            result = _extract_number_and_supplment_from_issue_element("Supl. 1")
            test_cases['test12'] = result
        except Exception as error:
            result = ''
            test_cases['test12'] = type(error).__name__
        return expected== result


    def t13():
        expected = None, "0"
        try:
            result = _extract_number_and_supplment_from_issue_element("Suppl")
            test_cases['test13'] = result
        except Exception as error:
            result = ''
            test_cases['test13'] = type(error).__name__
        return expected== result


    def t14():
        expected = None, "12"
        try:
            result = _extract_number_and_supplment_from_issue_element("Suppl 12")
            test_cases['test14'] = result
        except Exception as error:
            result = ''
            test_cases['test14'] = type(error).__name__
        return expected== result


    def t15():
        expected = None, "2"
        try:
            result = _extract_number_and_supplment_from_issue_element("s2")
            test_cases['test15'] = result
        except Exception as error:
            result = ''
            test_cases['test15'] = type(error).__name__
        return expected== result


    def t16():
        expected = "spe", None
        try:
            result = _extract_number_and_supplment_from_issue_element("spe")
            test_cases['test16'] = result
        except Exception as error:
            result = ''
            test_cases['test16'] = type(error).__name__
        return expected== result


    def t17():
        expected = "spe", None
        try:
            result = _extract_number_and_supplment_from_issue_element("Especial")
            test_cases['test17'] = result
        except Exception as error:
            result = ''
            test_cases['test17'] = type(error).__name__
        return expected== result


    def t18():
        expected = "spe1", None
        try:
            result = _extract_number_and_supplment_from_issue_element("spe 1")
            test_cases['test18'] = result
        except Exception as error:
            result = ''
            test_cases['test18'] = type(error).__name__
        return result == expected


    def t19():
        expected = "spepr", None
        try:
            result = _extract_number_and_supplment_from_issue_element("spe pr")
            test_cases['test19'] = result
        except Exception as error:
            result = ''
            test_cases['test19'] = type(error).__name__
        return expected == result


    def t20():
        expected = "spe2", None
        try:
            result = _extract_number_and_supplment_from_issue_element("spe2")
            test_cases['test20'] = result
        except Exception as error:
            result = ''
            test_cases['test20'] = type(error).__name__
        return result == expected


    def t21():
        expected = "spe2", None
        try:
            result = _extract_number_and_supplment_from_issue_element("spe.2")
            test_cases['test21'] = result
        except Exception as error:
            result = ''
            test_cases['test21'] = type(error).__name__
        return result == expected


    def t22():
        expected = None, "1"
        try:
            result = _extract_number_and_supplment_from_issue_element("supp 1")
            test_cases['test22'] = result
        except Exception as error:
            result = ''
            test_cases['test22'] = type(error).__name__
        return result == expected


    def t23():
        expected = None, "0"
        try:
            result = _extract_number_and_supplment_from_issue_element("suppl")
            test_cases['test23'] = result
        except Exception as error:
            result = ''
            test_cases['test23'] = type(error).__name__
        return result == expected


    def t24():
        expected = None, "1"
        try:
            result = _extract_number_and_supplment_from_issue_element("suppl 1")
            test_cases['test4'] = result
        except Exception as error:
            result = ''
            test_cases['test4'] = type(error).__name__
        return result == expected


    def t25():
        expected = None, "12"
        try:
            result = _extract_number_and_supplment_from_issue_element("suppl 12")
            test_cases['test25'] = result
        except Exception as error:
            result = ''
            test_cases['test25'] = type(error).__name__
        return result == expected


    def t26():
        expected = None, "1-2"
        try:
            result = _extract_number_and_supplment_from_issue_element("suppl 1-2")
            test_cases['test26'] = result
        except Exception as error:
            result = ''
            test_cases['test26'] = type(error).__name__
        return result == expected


    def t27():
        expected = None, "1"
        try:
            result = _extract_number_and_supplment_from_issue_element("suppl. 1")
            test_cases['test27'] = result
        except Exception as error:
            result = ''
            test_cases['test27'] = type(error).__name__
        return result == expected

    try :

        # if not t1() or not t2() or not t3() or not t4() or not t5() \
        #       or  not t6() or not t7() or not t8() or not t9() or not t10() \
        #            or     not t11() or not t12() or not t13() or not t14() or not t15()\
        #     or  not t16() or not t17() or not t18() or not t19() or not t20() \
        #         or not t21() or not t22() or not t23() or not t24() or not t25() or not t26() or not t27():
        #     isT=False
        numberOfTestCases = (t1()+t2()+t3()+t4()+t5()+t6()+t7()+t8()+t9()+t10()+t11()+t12()
                        +t13()+t14()+t15()+t16()+t17()+t18()+t19()+t20()+t21()
                         +t22()+t23()+t24()+t25()+t26()+t27())
        print(test_cases)
    except Exception as error :
        print(test_cases)




