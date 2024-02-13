# function GetVersion {
#     $data = Get-Content -Path .\command_data.txt
#     # Write-Host $data
#     $datePattern = [Regex]::new('sprt:A\s+\|\s+0x[0-9a-z]+\s+\|\s+[0-9.]+\s[a-zA-Z]+\s+\|\s+(\d+.\d+.\d+.\d+)\s+')
#     $matches = $datePattern.Matches($data)
#     $mat = [string]$matches
#     $datePattern = [Regex]::new('\d\.\d+.\d+.\d+')
#     $ver = $datePattern.Matches($mat)
#     # Write-Host $ver
#     return $ver
# }

# if(10 -eq  10){
#     Write-Host  Test
#     exit
# }


$data = '{"Build": "1.12.32.123","Commit": "4fsdfrsd","PackageVersion": "1.30.1.254_5fsrgd78"}'
Write-Host $data
$datePattern = [Regex]::new('"Build":\s+\"(\d+.\d+.\d+.\d+)",')
$matches = $datePattern.Matches($data)
$ver = $matches.Groups[1].Value
Write-Host $ver.getType().Name
