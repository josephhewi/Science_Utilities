use strict;
use warnings;

# determine which files to read and output to
my $target_file = "$ARGV[0]";
my $output_file = $ARGV[0] . "_grep";

# read file to array
open (FILE, "$target_file") or die "cannot open the associated test file\n";
my @data = (<FILE>);
close (FILE);

# open output file
open(my $prgm_output, ">", "$output_file");

# length of array, grep search criteria
my $size = scalar(@data);
my $search  = "cell  [0-9]\{5}";
my $out;

for ( my $i = 0; $i < $size + 1; $i = $i + 1 ){
	$out = grep {/$search/} ($data[$i]);
	if ($out > 0){
		print $prgm_output "$data[$i+1]"; # output line following grep criteria
		print "$data[$i+1]"; # print line to cmd
	}
}
