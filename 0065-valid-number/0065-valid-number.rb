# @param {String} s
# @return {Boolean}
def is_number(s)
  /^[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$/.match?(s)
end