class Solution {
    func isNumber(_ s: String) -> Bool {
        
        let sign = "[+-]?"
        let digits = "[0-9]+"
        
        let integer = "\(sign)\(digits)"
        let decimal = "\(sign)(?:\(digits)\\.|\(digits)\\.\(digits)|\\.\(digits))"
    
        let valid = "(?:\(decimal)|\(integer))([eE]\(integer))?"
        
        return s.range(of: "^\(valid)$", options: .regularExpression) != nil
    }
}