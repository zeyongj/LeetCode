import scala.util.{Failure, Success, Try}
object Solution {
    def isNumber(s: String): Boolean = {
        Try(s.toDouble) match {
          case Success(_) =>
            s.filter(_.isLetter).forall(_.toLower == 'e')
          case Failure(_) => false
    }
  }
}
